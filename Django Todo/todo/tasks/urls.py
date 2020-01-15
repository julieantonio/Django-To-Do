from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='list'), #'' rep home page, views triggers http response
  path('update_task/<str:pk>/', views.updateTask, name='update_task'),  # dynamic url primary key, allows call url pattern
  path('delete_task/<str:pk>/', views.deleteTask, name='delete_task')
]