from django.urls import path,include

from .views import todo_list_create, todo_detail, TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView
urlpatterns = [
   # path("todos/",todo_list_create),
   # path("todos/<int:pk>/",todo_detail)

   path("todos/",TodoListCreateAPIView.as_view()),
   path("todos/<int:pk>/",TodoRetrieveUpdateDestroyAPIView.as_view())
]