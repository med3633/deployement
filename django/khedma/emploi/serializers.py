from .models import Emploi, Categorie
from rest_framework import serializers

class EmploiSerializers(serializers.ModelSerializer):
    image_emploi = serializers.ImageField(required=False)  # Add this line

    class Meta:
        model = Emploi
        fields = '__all__'

class CreerEmploiSerializer(serializers.ModelSerializer):
    image_emploi = serializers.ImageField(required=False)  # Add this line

    class Meta:
        model = Emploi
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
