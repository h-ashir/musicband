from django.shortcuts import render, redirect
import datetime
import functools
from django.contrib import messages
from TicketApp.models import Ticket
from App.models import Event
from TicketApp.forms import CreateTicketForm, UpdateTicketForm
from django.contrib.auth.decorators import login_required


def ticketbase(request):
    return render(request, 'TicketApp/ticketbase.html')

#viewing ticket details

def ticket_Details(request, pk):
    ticket = Ticket.objects.get(pk = pk)
    context = {
        'ticket': ticket
    }
    return render(request, 'TicketApp/ticket_details.html', context)

#For customers

#Creating tickets
@login_required
def create_Ticket(request, pk):
    events = Event.objects.get(pk = pk)
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.event_title = events
            ticket.created_by = request.user
            ticket.ticket_status = 'Pending'
            ticket.save()
            messages.info(request, 'Your Ticket request has been submitted')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong !!')
            print(form.errors)
            return redirect('events')
            
    else:
        form = CreateTicketForm()
        context = {
            'form' : form,
            'events': events
            }
    return render(request, 'TicketApp/create_ticket.html', context)


def update_Ticket(request, pk):
    ticket = Ticket.objects.get(pk = pk)
    if request.method == 'POST':
        form  = UpdateTicketForm(request.POST, instance = ticket)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your ticket has been updated.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong !! Please try again')
            # return redirect('dashboard')
    else:
        form =  UpdateTicketForm(instance = ticket)
        context = {
            'form': form
        }
        return render(request, 'TicketApp/update_ticket.html', context)
    


def all_Tickets(request):
    tickets = Ticket.objects.filter(created_by = request.user).order_by('-date_created')
    context = {
        'tickets': tickets
    }
    return render(request, 'TicketApp/all_tickets.html', context)


#For engineers


def engineer_required(f, redirect_url ="TicketApp:all_tickets"):
    @functools.wraps(f)
    def wrapper(request, *args, **kwargs):
        print('wrapper()')
        if request.user.is_authenticated:
            if request.user.is_engineer:
                return f(request, *args, **kwargs)
            else:
                return redirect("/")
        else:
            return redirect("/")
        print(f"args : {args}")
        print(f"kwargs : {kwargs}")

    return wrapper


#view tickets
@engineer_required
def ticket_Queue(request):
    tickets = Ticket.objects.filter(ticket_status = 'Pending')
    context = {
        'tickets': tickets
    }
    return render(request, 'TicketApp/ticket_queue.html', context)

#Accept tickets
def accept_Ticket(request, pk):
    ticket = Ticket.objects.get(pk = pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been accepted.')
    return redirect('workspace')

#close tickets
def close_Ticket(request, pk):
    ticket = Ticket.objects.get(pk = pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been closed.')
    return redirect('ticket_queue')

#Ticket engineer is working on
@engineer_required
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to = request.user, is_resolved = False).order_by('-accepted_date')
    context = {
        'tickets': tickets
    }
    return render(request, 'TicketApp/workspace.html', context)

def all_Closed_Tickets(request):
    tickets = Ticket.objects.filter(assigned_to = request.user, is_resolved = True)
    context = {
        'tickets': tickets
    }
    return render(request, 'TicketApp/all_closed_tickets.html', context)