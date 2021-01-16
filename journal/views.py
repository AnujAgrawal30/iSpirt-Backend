from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('last_update')
    http_method_names = ["get"]

    # If we get list, we only get names, but when it's an instance, we get all details.
    def get_serializer_class(self):
        if self.get_view_name() == "Article Instance":
            return ArticleSerializer
        return ArticleNameSerializer
