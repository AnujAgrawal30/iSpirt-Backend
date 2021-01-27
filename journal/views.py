from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-last_update')
    http_method_names = ["get"]

    # If we get list, we only get names, but when it's an instance, we get all details.
    def get_serializer_class(self):
        if self.get_view_name() == "Article Instance":
            return ArticleSerializer
        return ArticleNameSerializer

@api_view(["GET"])
def get_article(request):
    article = Article.objects.get(name=request.GET['name'])
    response = ArticleSerializer(data=article, read_only=True)
    if response.is_valid:
        return Response(response.data)