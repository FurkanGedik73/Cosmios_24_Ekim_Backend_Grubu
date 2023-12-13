from django.urls import path,include

from rest_framework import routers

from .views import CategoryModelViewSet, BlogModelViewSet

router= routers.DefaultRouter()
router.register("category", CategoryModelViewSet)  #category/ category/<int:pk>/
router.register("blog", BlogModelViewSet)

urlpatterns = [
    # path("", include(router.urls))
] + router.urls