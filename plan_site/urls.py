from rest_framework import permissions

from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from .views import *


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for Individual Plan Project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('', views.home, name='home'),

    path('generate-report/', GenerateReport.as_view(), name='generate-report'),

    path('plans/', PlanList.as_view(), name='plan_list'),
    path('plans/<int:pk>/', PlanDetail.as_view(), name='plan_detail'),
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('reports/', ReportList.as_view(), name='report_list'),
    path('reports/<int:pk>/', ReportDetail.as_view(), name='report_detail'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
