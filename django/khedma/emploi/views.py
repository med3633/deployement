from django.shortcuts import render
from .models import Emploi, Categorie
from users.models import UserAccount, Personne, Societe
from Abonnement.models import *
from rest_framework import viewsets
from .serializers import EmploiSerializers, CreerEmploiSerializer, CategoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers
from django.conf.urls import include 
from django.urls import path
# Create a router
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import date



class EmploisViewset(APIView):
    #@login_required
    def get(self, request):
        today = date.today()
        #delete expired emplois
        expired_emplois = Emploi.objects.filter(date_expiration__lt=today)
        expired_emplois.delete()

        queryset = Emploi.objects.all().order_by('is_archived').order_by('is_active')
        serializer = EmploiSerializers(queryset, many=True)
        return Response(serializer.data)
   
@api_view(['PUT']) 
def ArchiveEmploi(request, eid):
    emplois = Emploi.objects.get(pk = eid)
    emplois.is_archived = not emplois.is_archived
    emplois.save()
    msg = 'Emplois non archivé!'
    if (emplois.is_archived):
        msg = 'Emplois Archivé!'
    return Response({'message': msg}) 

@api_view(['PUT']) 
def PublieEmploi(request,eid):
    emplois = Emploi.objects.get(pk = eid)
    emplois.is_active = not emplois.is_active
    emplois.save()
    msg = 'Emplois caché!'
    if (emplois.is_active):
        msg = 'Emplois Publié!'
    return Response({'message': msg}) 

@api_view(['POST'])
def PublierEmploiView(request):
    if request.method == 'POST':
        emploi_data = request.data
        print(f"Request Data: {request.data}")  # Print request data for debugging purposes

        try:
            # Access uploaded image file
            image_file = request.FILES.get("image_emploi")

            # Get user from UserAccount model
            user_id = emploi_data['user_id']  # Use get to avoid KeyError
            user = UserAccount.objects.get(id=user_id)
            
            # Create new emploi object
            new_emploi = Emploi.objects.create(
                titre=emploi_data['titre'],
                description=emploi_data['description'],
                date_postulation=emploi_data['date_postulation'],
                date_expiration=emploi_data['date_expiration'],
                duree_offre=emploi_data['duree_offre'],
                genre_demande=emploi_data['genre_demande'],
                intervalle_age=emploi_data['intervalle_age'],
                localisation=emploi_data['localisation'],
                montant_paiement=emploi_data['montant_paiement'],
                experience=emploi_data['experience'],
                region=emploi_data['region'],
                type_emploi=emploi_data['type_emploi'],
                user=user,
                image_emploi=image_file,  
            )

            # Process categories
            categories_ids = emploi_data.getlist('categories', [])  # Get category IDs from request data
            print(f"Received categories IDs: {categories_ids}")  # Print received category IDs for debugging
            valid_categories = Categorie.objects.filter(pk__in=[int(id) for id in categories_ids])

            print("Valid categories retrieved from the database:")
            for category in valid_categories:
                print(category.nom)

            # Associate validated categories with new emploi object
            new_emploi.categories.set(valid_categories) 

            # Get category names for logging
            categories = [category.nom for category in valid_categories]

            # Get user's name for logging
            if user.role == 'societe':
                nom = user.societe.nom
            else:
                nom = f"{user.personne.nom} {user.personne.prenom}"
                
            # Construct email message
            image_url = f"{settings.MEDIA_ROOT}/images/favicon.ico"
            subject = "Une nouvelle offre d'emploi soumise: " + new_emploi.titre
            message = render_to_string(
                'emploi_notification.html',
                {'emploi': new_emploi, 'categories': ', '.join(categories), 'employeur': nom, 'email': user.email, 'image': image_url}
            )

            # Prepare email details
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            admins = UserAccount.objects.filter(role='admin')
            recipient_list.extend([admin.email for admin in admins])

            # Send email
            send_mail(subject, message, from_email, recipient_list, html_message=message)

            # Serialize new emploi instance
            serializer = EmploiSerializers(new_emploi)  

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Log any exceptions that occur during processing
            print(f"An error occurred: {e}")

            # Return a 400 response if an error occurs
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)








@api_view(['GET'])
def GetEmplois(request, eid):
    emploi = Emploi.objects.get(pk = eid)
    serializer = EmploiSerializers(emploi)
    return Response(serializer.data)

@api_view(['PUT'])
def PutEmplois(request, eid):
    emploi = Emploi.objects.get(pk = eid)
    emploi_data = request.data
    print(emploi_data)
    emploi.titre= emploi_data['titre']
    emploi.description= emploi_data['description']
    emploi.date_postulation= emploi_data['date_postulation']
    emploi.date_expiration= emploi_data['date_expiration']
    emploi.duree_offre= emploi_data['duree_offre']
    emploi.genre_demande= emploi_data['genre_demande']
    emploi.intervalle_age= emploi_data['intervalle_age']
    emploi.localisation= emploi_data['localisation']
    emploi.montant_paiement= emploi_data['montant_paiement']
    emploi.experience= emploi_data['experience']
    emploi.region= emploi_data['region']
    emploi.type_emploi= emploi_data['type_emploi']
    user = UserAccount.objects.get(pk = emploi_data['user_id'])
    if (user):
        emploi.user = user
    emploi.save()
    return Response({'message': 'Emploi Modifié'})  
    #image_emploi=image_file,  # Save the image file using the ImageField


class getCategoriesView(APIView):
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_emploi(request, emploi_id):
    try:
        emploi = Emploi.objects.get(pk=emploi_id)
    except Emploi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        emploi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        parent = request.data.get('parent')
        if parent is not None:
            parent = Categorie.objects.get(pk = request.data['parent'])
        slug = request.data.get('slug')
        description = request.data.get('description')
        category = Categorie.objects.create(
            nom= request.data["nom"],
            slug= slug,
            description = description,
            parent = parent
            )
        return Response({'message': 'Catégorie créer'})
    
    def delete(self,request):
        print(request.data)
        category = Categorie.objects.get(pk=request.data['id'])
        category.delete()
        return Response({'message': 'Catégorie supprimé avec succés!'})
    
    def put(self,request):
        data = request.data['data']
        category = Categorie.objects.get(pk = data['id'])
        category.nom = data["nom"]
        category.slug = data["slug"]
        category.description = data['description']
        parent = data.get('parent')
        if parent is not None:
            parent = Categorie.objects.get(pk = data['parent']) 
        category.parent = parent
        category.save()
        return Response({'message': 'Catégorie Modifier avec succéss!'})
    

 