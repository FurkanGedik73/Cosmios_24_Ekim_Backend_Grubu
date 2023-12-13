from django.urls import path,include

from .views import todo_list, todo_detail
urlpatterns = [
   path("todos/",todo_list),
   path("todos/<int:pk>/",todo_detail)
]