from django.urls import path
from TicketApp import views
urlpatterns = [
    
    path('ticketbase/', views.ticketbase, name = 'ticketbase'),
    path('ticket_details/<int:pk>/', views.ticket_Details, name = 'ticket_details'),
    path('create_ticket/<int:pk>/', views.create_Ticket, name = 'create_ticket'),
    # path('update_ticket/<int:pk>', views.update_Ticket, name = 'update_ticket'),
    path('all_tickets/', views.all_Tickets, name = 'all_tickets'),
    path('ticket_queue/', views.ticket_Queue, name = 'ticket_queue'),
    path('accept_ticket/<int:pk>', views.accept_Ticket, name = 'accept_ticket'),
    # path('close_ticket/<int:pk>', views.close_Ticket, name = 'close_ticket'),
    path('workspace/', views.workspace, name = 'workspace'),
    path('all_closed_tickets/', views.all_Closed_Tickets, name = 'all_closed_tickets'),
    
]