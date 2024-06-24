from django.urls import path
from . import views

urlpatterns = [
    path('estado', views.estado_registro_list, name='estado_registro_list'),
    path('estado/new/', views.estado_registro_create, name='estado_registro_create'),
    path('estado/<int:pk>/edit/', views.estado_registro_update, name='estado_registro_update'),
    path('estado/<int:pk>/delete/', views.estado_registro_delete, name='estado_registro_delete'),
]