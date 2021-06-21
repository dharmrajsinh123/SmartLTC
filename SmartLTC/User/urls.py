from django.contrib import admin
from django.urls import path,include

from . import views
from .views import *
from knox import views as knox_views
# from import models*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


   #for token confirm and validate_token
    path('password_reset/confirm', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/validate_token', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('Account/', views.UserViewSet.as_view()),
    # path('Account/', views.UserViewSet.as_view()),

]
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# urlpatterns = [
#   path('auth/', include('rest_auth.urls')),
# ]