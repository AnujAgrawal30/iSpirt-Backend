from rest_framework import serializers
from .models import *

class ArticleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'tags']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1