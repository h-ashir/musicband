from django.db import models
from user.models import User
import uuid
# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length = 30, blank = False, null = False)
    event_description = models.CharField(max_length=255)
    event_image = models.ImageField(upload_to='events')
    event_venue = models.CharField(max_length=100, blank=True, null=True)
    event_date = models.DateField()
    event_time = models.TimeField() 
    def __str__(self):
        return self.event_title
    
class Booking(models.Model):
    person_name = models.CharField(max_length=30, blank=False, null=False)
    person_mail = models.EmailField()
    person_address = models.CharField(max_length=100, blank=False, null=False)
    person_number = models.CharField(max_length=15, blank=False, null=False)
    event_title = models.ForeignKey(Event, on_delete=models.CASCADE)
    person_count = models.IntegerField(blank=False, null=False)
    booking_on = models.DateField(auto_now=True)


# class Ticket(models.Model):
#     status_choice = (
#         'Active', 'Active',
#         'Completed', 'Completed',
#         'Pending', 'Pending'
#     )
#     ticket_number = models.UUIDField(default = uuid.uuid4)
#     event_title = models.ForeignKey(Event, on_delete = models.CASCADE)
#     number_of_person = models.IntegerField(blank = False, null = False)
#     person_mail_address = models.EmailField()
#     person_mobile_number = models.IntegerField()
#     person_count = models.IntegerField()
#     created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'created_by')
#     date_created = models.DateTimeField(auto_now_add = True)
#     assigned_to = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True, blank = True)
#     is_resolved = models.BooleanField(default = False)
#     accepted_date = models.DateTimeField(null = True, blank = True)
#     closed_date = models.DateTimeField(null = True, blank = True)
#     ticket_status = models.CharField(max_length = 50)
#     def __str__(self):
#         return self.event_title



class Music(models.Model):
    song_title = models.CharField(max_length=100)
    song_description = models.TextField()
    song_link_youtube = models.TextField()
    def __str__(self):
        return self.song_title

class Team(models.Model):
    member_name = models.CharField(max_length=30)
    member_label = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='team')
    member_description = models.TextField()
    member_playlist = models.TextField()
    def __str__(self):
        return self.member_name

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.CharField(max_length=255)
    def __str__(self):
        return self.name
