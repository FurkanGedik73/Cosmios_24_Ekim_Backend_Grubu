from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import SearchFilter , OrderingFilter


class StudentModelViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = CustomPageNumberPagination  # devre dışı bırakarak LimitOffsetPagination'ın devreye girmesini sağlarız. 
    # pagination_class = CustomCursorPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  #Bu işlemden dolayı globaldeki orderin işlemi yapılamadı  çünkü önce local dikkate alınır. Local için de parantez içerisinde ordering i import ederiz.  

    filterset_fields = ["first_name","last_name"]
    search_fields = ["first_name", "last_name"]    # ForeignKey alanları kullanılamaz. Path hata verir. 

class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    # pagination_class = CustomLimitOffsetPagination

    filterset_fields = ["path_name"]
    search_fields = ["path_name"]  