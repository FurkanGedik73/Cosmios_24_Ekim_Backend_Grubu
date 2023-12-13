from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

from rest_framework.viewsets import ModelViewSet


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer