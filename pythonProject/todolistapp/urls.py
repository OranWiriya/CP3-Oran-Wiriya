from django.urls import path
from todolistapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about),
    path('todolist/', views.todolist, name='todolist'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
]
