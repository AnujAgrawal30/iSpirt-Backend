from rest_framework import serializers
import markdown

from .models import *

class ArticleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'tags']

class ArticleSerializer(serializers.ModelSerializer):
    content_html = serializers.SerializerMethodField()
    abstract_html = serializers.SerializerMethodField()

    class Meta:
        model = Article
        # fields = '__all__'
        depth = 1
        exclude = ('content', 'abstract')
    
    def get_content_html(self, obj):
        return get_html(obj.content)
    
    def get_abstract_html(self, obj):
        return get_html(obj.abstract)

def get_html(md):
    html = markdown.markdown(md)
    return html
