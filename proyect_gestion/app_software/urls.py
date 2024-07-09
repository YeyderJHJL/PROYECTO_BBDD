from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('estado', views.estado_registro_list, name='estado_registro_list'),
    path('estado/new/', views.estado_registro_create, name='estado_registro_create'),
    path('estado/<int:pk>/edit/', views.estado_registro_update, name='estado_registro_update'),
    path('estado/<int:pk>/delete/', views.estado_registro_delete, name='estado_registro_delete'),
    
    path('tipo_cliente', views.tipo_cliente_list, name='tipo_cliente_list'),
    path('tipo_cliente/new/', views.tipo_cliente_create, name='tipo_cliente_create'),
    path('tipo_cliente/<int:pk>/edit/', views.tipo_cliente_update, name='tipo_cliente_update'),
    path('tipo_cliente/<int:pk>/delete/', views.tipo_cliente_delete, name='tipo_cliente_delete'),

    path('estado_cliente', views.estado_cliente_list, name='estado_cliente_list'),
    path('estado_cliente/new/', views.estado_cliente_create, name='estado_cliente_create'),
    path('estado_cliente/<int:pk>/edit/', views.estado_cliente_update, name='estado_cliente_update'),
    path('estado_cliente/<int:pk>/delete/', views.estado_cliente_delete, name='estado_cliente_delete'),

    path('tipo_proyecto', views.tipo_proyecto_list, name='tipo_proyecto_list'),
    path('tipo_proyecto/new/', views.tipo_proyecto_create, name='tipo_proyecto_create'),
    path('tipo_proyecto/<int:pk>/edit/', views.tipo_proyecto_update, name='tipo_proyecto_update'),
    path('tipo_proyecto/<int:pk>/delete/', views.tipo_proyecto_delete, name='tipo_proyecto_delete'),

    path('estado_proyecto', views.estado_proyecto_list, name='estado_proyecto_list'),
    path('estado_proyecto/new/', views.estado_proyecto_create, name='estado_proyecto_create'),
    path('estado_proyecto/<int:pk>/edit/', views.estado_proyecto_update, name='estado_proyecto_update'),
    path('estado_proyecto/<int:pk>/delete/', views.estado_proyecto_delete, name='estado_proyecto_delete'),

    path('etapas_proyecto', views.etapas_proyecto_list, name='etapas_proyecto_list'),
    path('etapas_proyecto/new/', views.etapas_proyecto_create, name='etapas_proyecto_create'),
    path('etapas_proyecto/<int:pk>/edit/', views.etapas_proyecto_update, name='etapas_proyecto_update'),
    path('etapas_proyecto/<int:pk>/delete/', views.etapas_proyecto_delete, name='etapas_proyecto_delete'),

    path('actividad', views.actividad_list, name='actividad_list'),
    path('actividad/new/', views.actividad_create, name='actividad_create'),
    path('actividad/<int:pk>/edit/', views.actividad_update, name='actividad_update'),
    path('actividad/<int:pk>/delete/', views.actividad_delete, name='actividad_delete'),

    path('complejidad', views.complejidad_list, name='complejidad_list'),
    path('complejidad/new/', views.complejidad_create, name='complejidad_create'),
    path('complejidad/<int:pk>/edit/', views.complejidad_update, name='complejidad_update'),
    path('complejidad/<int:pk>/delete/', views.complejidad_delete, name='complejidad_delete'),

    path('cargos_proyecto', views.cargosproyecto_list, name='cargos_proyecto_list'),
    path('cargos_proyecto/new/', views.cargosproyecto_create, name='cargos_proyecto_create'),
    path('cargos_proyecto/<int:pk>/edit/', views.cargosproyecto_update, name='cargos_proyecto_update'),
    path('cargos_proyecto/<int:pk>/delete/', views.cargosproyecto_delete, name='cargosproyecto_delete'),

    path('cargos_personal', views.cargos_personal_list, name='cargos_personal_list'),
    path('cargos_personal/new/', views.cargos_personal_create, name='cargos_personal_create'),
    path('cargos_personal/<int:pk>/edit/', views.cargos_personal_update, name='cargos_personal_update'),
    path('cargos_personal/<int:pk>/delete/', views.cargos_personal_delete, name='cargos_personal_delete'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/new/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),

]