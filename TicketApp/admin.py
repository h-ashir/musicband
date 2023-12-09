from django.contrib import admin
from .models import Ticket
# Register your models here.
class TicketContent(admin.ModelAdmin):
    list_display = ('event_title', 'ticket_number', 'number_of_person','person_mobile_number', 'created_by','assigned_to', 'accepted_date')
admin.site.register(Ticket, TicketContent)


