from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:id>/',views.edit_user,name='edit_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    
]