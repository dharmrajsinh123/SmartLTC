from django.contrib import admin
from django.urls import path,include
from . import views
from knox import views as knox_views
urlpatterns = [
    path('Store/', views.StoreViewSet.as_view()),
    path('Store/<int:id>/', views.StoreViewSet.as_view()),

    path('role_mst/', views.role_mstViewSet.as_view()),
    path('user_mst/', views.user_mstViewSet.as_view()),
    # path('role_mst/<int:id>/', views.role_mstViewSet.as_view()),

]