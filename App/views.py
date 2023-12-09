from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from App.models import Event, Music, Team, Contact, Booking
import datetime
from App.forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'App/index.html')

def about(request):
    return render(request, 'App/about.html')

# @login_required()
def events(request):
    dict_event = {
        'events': Event.objects.all()
    }
    return render(request, 'App/events.html',dict_event)

@login_required()
def booking(request, pk):
    event_details = Event.objects.get(pk = pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = BookingForm()
        dict_booking = {
            'form': form,
            'event_details': event_details,
        }
    return render(request, 'App/booking.html', dict_booking)

def music(request):
    dict_music = {
        'music': Music.objects.all()
    }
    return render(request, 'App/music.html', dict_music)

def team(request):
    dict_team = {
        'team': Team.objects.all()
    }
    return render(request, 'App/team.html', dict_team)

def confirmation(request):
    name = request.user
    context = {'name':name}
    return render(request, 'App/confirmation.html', context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if len(message) < 4:
            return HttpResponse("Enter a valid message")
        else:    
            newContact = Contact(name=name, email=email, message=message)
            newContact.save()
    return render(request, 'App/contact.html')

# ------------------------------------------------------------------------------------------

# def ticketbase(request):
#     return render(request, 'App/ticketbase.html')

# def ticket_Details(request):
#     ticket = Booking.objects.all()
#     context = {
#         'ticket': ticket
#     }
#     return render(request, 'App/ticket_details.html', context)

# def create_Ticket(request):
#     if request.method == 'POST':
#         pass