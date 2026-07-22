from django.urls import path
from . import views

urlpatterns = [

    path('raise-ticket/', views.raise_ticket, name='raise_ticket'),
    path('my-tickets/',views.my_tickets,name='my_tickets'),
    path('ticket/<int:id>/',views.ticket_detail,name='ticket_detail'),
    path('all-tickets/',views.all_tickets,name='all_tickets'),
    path('admin-ticket/<int:id>/',views.admin_ticket_detail,name='admin_ticket_detail'),
    path('assigned-tickets/',views.assigned_tickets,name='assigned_tickets'),
    path('engineer-ticket/<int:id>/',views.engineer_ticket_detail,name='engineer_ticket_detail'),

]