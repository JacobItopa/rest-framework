from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'custom_id',
            'category',
            'publish_date',
            'last_updated',
            )