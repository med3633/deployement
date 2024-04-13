from rest_framework import serializers
from .models import Chat
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'  # You can specify the fields you want to include here if needed


        