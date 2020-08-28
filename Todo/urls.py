from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('addTodo',views.addTodo),
    path('deleteTodo/<int:todo_id>',views.deleteTodo),
]