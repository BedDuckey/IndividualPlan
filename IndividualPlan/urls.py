from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('plan_site.urls')),  # Подключение маршрутов из приложения `plan_site`
]