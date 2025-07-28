from rest_framework import serializers
from backend.models import images
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= images 
        fields =['name','email']