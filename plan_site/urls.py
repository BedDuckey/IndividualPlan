from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # План
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/create/', views.plan_create, name='plan_create'),
    path('plans/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('plans/<int:pk>/update/', views.plan_update, name='plan_update'),
    path('plans/<int:pk>/delete/', views.plan_delete, name='plan_delete'),

    # Задача
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Пользователь
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # Отчет
    path('reports/', views.report_list, name='report_list'),
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('reports/<int:pk>/update/', views.report_update, name='report_update'),
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),
]
