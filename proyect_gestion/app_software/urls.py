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

    path('actividades_complejidad', views.actividades_complejidad_list, name='actividades_complejidad_list'),
    path('actividades_complejidad/new/', views.actividades_complejidad_create, name='actividades_complejidad_create'),
    path('actividades_complejidad/<int:pk>/edit/', views.actividades_complejidad_update, name='actividades_complejidad_update'),
    path('actividades_complejidad/<int:pk>/delete/', views.actividades_complejidad_delete, name='actividades_complejidad_delete'),

    path('etapa_actividad', views.etapa_actividad_list, name='etapa_actividad_list'),
    path('etapa_actividad/new/', views.etapa_actividad_create, name='etapa_actividad_create'),
    path('etapa_actividad/<int:pk>/edit/', views.etapa_actividad_update, name='etapa_actividad_update'),
    path('etapa_actividad/<int:pk>/delete/', views.etapa_actividad_delete, name='etapa_actividad_delete'),

    path('incidencia_personal', views.incidencia_personal_list, name='incidencia_personal_list'),
    path('incidencia_personal/new/', views.incidencia_personal_create, name='incidencia_personal_create'),
    path('incidencia_personal/<int:pk>/edit/', views.incidencia_personal_update, name='incidencia_personal_update'),
    path('incidencia_personal/<int:pk>/delete/', views.incidencia_personal_delete, name='incidencia_personal_delete'),

    path('incidencias', views.incidencias_list, name='incidencias_list'),
    path('incidencias/new/', views.incidencias_create, name='incidencias_create'),
    path('incidencias/<int:pk>/edit/', views.incidencias_update, name='incidencias_update'),
    path('incidencias/<int:pk>/delete/', views.incidencias_delete, name='incidencias_delete'),

    path('personal', views.personal_list, name='personal_list'),
    path('personal/new/', views.personal_create, name='personal_create'),
    path('personal/<int:pk>/edit/', views.personal_update, name='personal_update'),
    path('personal/<int:pk>/delete/', views.personal_delete, name='personal_delete'),

    path('personal_actividad', views.personal_actividad_list, name='personal_actividad_list'),
    path('personal_actividad/new/', views.personal_actividad_create, name='personal_actividad_create'),
    path('personal_actividad/<int:pk>/edit/', views.personal_actividad_update, name='personal_actividad_update'),
    path('personal_actividad/<int:pk>/delete/', views.personal_actividad_delete, name='personal_actividad_delete'),

    path('personal_cargos_personal', views.personal_cargos_personal_list, name='personal_cargos_personal_list'),
    path('personal_cargos_personal/new/', views.personal_cargos_personal_create, name='personal_cargos_personal_create'),
    path('personal_cargos_personal/<int:pk>/edit/', views.personal_cargos_personal_update, name='personal_cargos_personal_update'),
    path('personal_cargos_personal/<int:pk>/delete/', views.personal_cargos_personal_delete, name='personal_cargos_personal_delete'),

    path('personal_cargos_proyecto', views.personal_cargos_proyecto_list, name='personal_cargos_proyecto_list'),
    path('personal_cargos_proyecto/new/', views.personal_cargos_proyecto_create, name='personal_cargos_proyecto_create'),
    path('personal_cargos_proyecto/<int:pk>/edit/', views.personal_cargos_proyecto_update, name='personal_cargos_proyecto_update'),
    path('personal_cargos_proyecto/<int:pk>/delete/', views.personal_cargos_proyecto_delete, name='personal_cargos_proyecto_delete'),

    path('proyecto', views.proyecto_list, name='proyecto_list'),
    path('proyecto/new/', views.proyecto_create, name='proyecto_create'),
    path('proyecto/<int:pk>/edit/', views.proyecto_update, name='proyecto_update'),
    path('proyecto/<int:pk>/delete/', views.proyecto_delete, name='proyecto_delete'),

]