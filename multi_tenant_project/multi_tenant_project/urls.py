"""
URL configuration for multi_tenant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import TodoViewSet, UserRegistrationView  
from rest_framework.routers import DefaultRouter
from project_management.views import ProjectViewSet, TaskViewSet
from .views import api_root

# Set up DRF router
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistrationView.as_view(), name='register'),  # Register URL
    path('api/', api_root, name='api_root'),  # Include the API root path
    path('api/', include(router.urls)),  # Include router URLs
]
