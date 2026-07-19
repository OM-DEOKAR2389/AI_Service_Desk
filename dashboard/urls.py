from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    path("user/", views.user_dashboard, name="user_dashboard"),
    path("engineer/", views.engineer_dashboard, name="engineer_dashboard"),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.user_list, name='user_list'),
]