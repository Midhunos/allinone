from django.urls import path
from .views import CreateTodo,GetUpdate
urlpatterns = [
      path('tasks/',CreateTodo.as_view(),name="create"),
      path('tasks/<int:pk>/',GetUpdate.as_view(),name="update")
    
]