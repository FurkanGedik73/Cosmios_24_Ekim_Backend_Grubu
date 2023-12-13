from django.shortcuts import render

from  rest_framework import viewsets

from .models import Category, Blog
from .serializer import CategorySerializer , BlogSerializer

# Create your views here.

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer