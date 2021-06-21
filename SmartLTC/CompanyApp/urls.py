from django.contrib import admin
from django.urls import path,include
from . import views
from knox import views as knox_views
urlpatterns = [
    path('Company/', views.CompanyViewSet.as_view()),
    path('Company/<int:id>/', views.CompanyViewSet.as_view()),

]
