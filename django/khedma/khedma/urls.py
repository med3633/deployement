from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from users.views import updateStatusSociete, PersonneCreateView, SocieteCreateView,EnregistrerCandidatRatingView,UserActivationView, PersonneDetailView,SocieteDetailView,getSocietesView,getCandidatsView, ModifierPersonneView, ModifierSocieteView
from users.views import PersonneCreateView, SocieteCreateView,EnregistrerCandidatRatingView,UserActivationView, PersonneDetailView,SocieteDetailView,getSocietesView, ModifierPersonneView, ModifierSocieteView, AdminView,AdminDetailView
from django.contrib.staticfiles.views import serve as staticfiles_serve
from users.views import get_rating_categories,get_moyennerating_societe,CompetenceCreateView,CompetencesByPersonneView,ModifierStatutRatingView,EnregistrerSocieteRatingView,get_moyennerating_candidat, add_competences_to_profile,delete_competence_from_profile
from users.views import ModifierStatutSocieteRatingView,change_password
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from emploi.views import *

from emploi import views
from khedma.middleware import EnforceHttpsMiddleware


from chat.views import CreateChatView,find_chat,user_chats ,GetMessagesView,AddMessageView,getUserChat,UserChats,FindChat


from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register(r'emploi', EmploisViewset)

urlpatterns = [
   

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('personne/', PersonneCreateView.as_view(), name='personne-create'),
    path('get_rating_categories/', get_rating_categories, name='get_rating_categories'),
    path('ajoutercompetenceaucandidat/',add_competences_to_profile,name='ajoutercompetencesaucandidat'),
    path('competence/',CompetenceCreateView.as_view(),name='competence'),
    path('listcandidats/',getCandidatsView.as_view(),name='liste-candidats'),
    path('listsocietes/',getSocietesView.as_view(),name='liste-societes'),
    path('personne/<int:pk>/competences/',CompetencesByPersonneView.as_view(),name='getCompetencesbypersonne'),
    path('donnerratingcandidat/',EnregistrerCandidatRatingView.as_view(),name='donnerratingcandidat'),
    path('donnerratingausociete/',EnregistrerSocieteRatingView.as_view(),name='donnerratingausociete'),
    path('auth/passwordchange/<int:user_id>/', change_password, name='change_password'),
   
    path('societe/', SocieteCreateView.as_view(), name='societe-create'),
    path('activate/<str:uid>/<str:token>/', UserActivationView.as_view(), name='user-activation'),
    path('personne/<int:pk>/', PersonneDetailView.as_view(), name='personne-detail'),
    path('societe/<int:pk>/', SocieteDetailView.as_view(), name='societe-detail'),
    path('modifierPersonne/<int:pk>/', ModifierPersonneView.as_view(), name='personne-modifier'),
    path('supprimercompetencecandidat/',delete_competence_from_profile,name='supprimercompetencecandidat'),
    path('societe/modifierSociete/<int:pk>/', ModifierSocieteView.as_view(), name='societe-modifier'),
    path('post-emploi',PublierEmploiView,name='poster-emploi'),
    path('archive-emploi/<int:eid>/', ArchiveEmploi, name='archive-emploi'),
    path('publie-emploi/<int:eid>/', PublieEmploi, name='publie-emploi'),
    path('societe-best/<int:sid>/', updateStatusSociete, name='societe-best'),
    path('get-emploi/<int:eid>/', GetEmplois, name='get-emploi'),
    path('put-emploi/<int:eid>/', PutEmplois, name='put-emploi'),
    path('get-emplois',EmploisViewset.as_view(),name='get-emplois'),
    path('get-categories', getCategoriesView.as_view(),name='getcategories'),
    path('delete-emploi/<int:emploi_id>/',delete_emploi, name='delete_emploi'),
    #path('',include(router.urls)),

    path('get_moyennerating_candidat/<int:idcandidat>/', get_moyennerating_candidat, name='get_moyennerating_candidat'),
    path('getmoyenneratingsociete/<int:idsociete>/',get_moyennerating_societe,name='getmoyenneratingsociete'),
    path('modifier-statut-rating/<int:rating_id>/', ModifierStatutRatingView.as_view(), name='modifier-statut-rating'),
    path('modifier-statutsociete-rating/<int:rating_id>/', ModifierStatutSocieteRatingView.as_view(), name='modifier-statutsociete-rating'),
    re_path(r'^static/(?P<path>.*)$', staticfiles_serve),
    path('api/', include("stripe_payment.urls")),
    #admin urls
    path('admin/users/', AdminView.as_view(), name='admin_views'),
    path('admin/users/<int:uid>/', AdminDetailView.as_view(), name='admin_detail_views'),
    path("Abonnement/", include("Abonnement.urls")),
    


    #chat url
   
    path('userChats/<int:user_id>/',UserChats.as_view(), name='userC'),
    path('find_chat/<int:first_id>/<int:second_id>/', FindChat.as_view(), name='find-chat'),
    path('getUserChat',getUserChat.as_view(), name='userChats'),
    path('api/chats/<int:userId>/',user_chats, name='user_chats'),
    path('chat/find/<int:firstId>/<int:secondId>/', find_chat, name='find_chat'),
    path('CreateChat/',CreateChatView.as_view(), name='CreateChat'),
    
    path('add-message/', AddMessageView.as_view(), name='add_message'),
    path('get-messages/<int:chat_id>/', GetMessagesView.as_view(), name='get_messages'),
   


    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


