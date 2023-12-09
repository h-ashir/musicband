from django.shortcuts import render, redirect
from user.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterCustomerForm
# Create your views here.

def registerCustomer(request):
    if request.method == 'POST':
        form  = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit = False)
            var.is_customer = True
            var.save()
            messages.info(request, 'Your account has been created successfully')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            return redirect('register')
    else:
        form = RegisterCustomerForm()
        context = {
            'form': form
        }
    return render(request, 'user/registerCustomer.html', context)

# Login a user
def loginCustomer(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)      #To check 
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request, 'Login Successful')
            try:
                return redirect(request.GET.get('next'))
            except:
                return redirect('home')
        else:
            messages.warning(request, 'Something went wrong !!')
            return redirect('login')
    else:
        return render(request, 'user/loginCustomer.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Please log in to continue !!')
    return redirect('home')