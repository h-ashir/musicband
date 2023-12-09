from django.db import models
from user.models import User
import uuid
from App.models import Event, Booking

# Create your models here.

class Ticket(models.Model):
    status_choice = (
        'Active', 'Active',
        'Completed', 'Completed',
        'Pending', 'Pending'
    )
    ticket_number = models.UUIDField(default = uuid.uuid4)
    event_title = models.ForeignKey(Event, on_delete = models.CASCADE, related_name='title_event')
    number_of_person = models.IntegerField(blank = False, null = False)
    person_mail_address = models.EmailField()
    person_mobile_number = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'created_by')
    date_created = models.DateTimeField(auto_now_add = True)
    assigned_to = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True, blank = True, related_name='assigned_to')
    is_resolved = models.BooleanField(default = False)
    accepted_date = models.DateTimeField(null = True, blank = True)
    closed_date = models.DateTimeField(null = True, blank = True)
    ticket_status = models.CharField(max_length = 50)
    # def __str__(self):
    #     return f"{self.event_title} - {self.person_mobile_number} - {self.number_of_person}"