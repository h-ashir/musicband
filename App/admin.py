from django.contrib import admin
from App.models import Event, Booking, Music, Team, Contact
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_title', 'event_image', 'event_description', 'event_venue', 'event_date', 'event_time')
admin.site.register(Event, EventAdmin)

class Content(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'person_mail', 'person_address', 'person_number', 'event_title', 'person_count', 'booking_on')
admin.site.register(Booking, Content)

admin.site.register(Music)

admin.site.register(Team)

class ContactContent(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
admin.site.register(Contact, ContactContent)

# admin.site.register(Ticket)