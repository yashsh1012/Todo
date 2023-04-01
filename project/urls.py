"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Custom user and todo api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up_api),
    path('profilapi/', views.profil_api),
   # path('profilapi/<int:id>', views.profil_api),
    path('login/', views.login_api),
    path('todo/', views.todo_api),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh' ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  
   
    
]
