from django.urls import path
from . import views

urlpatterns = [

    path('raise-ticket/', views.raise_ticket, name='raise_ticket'),
    path('my-tickets/',views.my_tickets,name='my_tickets'),
    path('ticket/<int:id>/',views.ticket_detail,name='ticket_detail'),

]