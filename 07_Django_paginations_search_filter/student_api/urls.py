from django.urls import path, include

from rest_framework import routers

from .views import(
    
    StudentModelViewset,
    PathModelViewSet,
    
    )

router = routers.DefaultRouter()
router.register("students" , StudentModelViewset)  #students/ student/id
router.register("paths", PathModelViewSet)


urlpatterns = [
    

] + router.urls

#urlpatterns += router.urls