from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('', views.support, name='support'),
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket_detail/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/create/', views.create_ticket, name='ticket_create'),  
]
