from django.shortcuts import render, redirect
from .models import Ticket, SystemUser, Feedback
from django.contrib import messages
from .forms import TicketForm, UserSignUpForm, FeedbackForm, SystemUserUpdateForm, TicketUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required


# Verify user types to restrict access to certain pages for different users
def is_dispatcher(user):
    return user.is_authenticated and user.role.dispatcher

def is_technician(user):
    return user.is_authenticated and user.role.technician

def is_company(user):
    return user.is_authenticated and user.role.company

def is_allowed(user):
    return user.is_authenticated


# Create your views here.
def home(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'home.html', {'feedbacks': feedbacks})
    

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return render(request, 'home.html')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'forms/login/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect( 'home')


# Managing Tickets
@login_required
def Ticket_registration(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.company = request.user
            ticket.save()
            messages.success(request, 'Your ticket has been created and is pending approval. You will be notified when it is approved.')
            return redirect('My_ticket_list')
        else:
            messages.warning(request, 'You have to be logged in as a company to create a ticket. If you are creating one on behalf of a company, please log in as a company.')
            return redirect('login')
    form = TicketForm()
    return render(request, 'forms/registrations/Ticket_registration.html', {'form': form})

def All_ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'lists/All_ticket_list.html', {'tickets': tickets})

def Ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'details/Ticket_detail.html', {'ticket': ticket})

def Update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Ticket has been updated')
            return redirect('My_ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'forms/updates/Ticket_update.html', {'form': form})

def Approve_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = 'Approved'
    ticket.dispatcher = request.user
    ticket.save()
    messages.success(request, 'Ticket has been approved')
    return redirect('approved_ticket_list')

def Accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = 'Accepted'
    ticket.technician = request.user
    ticket.save()

def Reject_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = 'Rejected'
    ticket.dispatcher = request.user
    ticket.save()

def Close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = 'Closed'
    ticket.technician = request.user
    ticket.save()

def Delete_ticket(request):
    ticket = Ticket.objects.get(pk=pk)
    ticket.delete()
    messages.success(request, 'Ticket deleted successfully')
    return redirect('All_ticket_list')

def Approved_ticket_list(request):
    tickets = Ticket.objects.filter(status='Approved')
    return render(request, 'lists/All_ticket_list.html', {'tickets': tickets})

def My_ticket_list(request):
    user = request.user
    if user.role == 'technician':
        tickets = Ticket.objects.filter(technician=user)
    elif user.role == 'dispatcher':
        tickets = Ticket.objects.filter(dispatcher=user)
    elif user.role == 'company':
        tickets = Ticket.objects.filter(company=user)
    else:
        return redirect('home')
    return render(request, 'lists/All_ticket_list.html', {'tickets': tickets})



# Managing Companies
def Company_registration(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.role = 'company'
            company.save()
            messages.success(request, 'Your company profile has been created, you can now login')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request, 'There was an error submitting your form. Please try again')
    else:
        form = UserSignUpForm()
    return render(request, 'forms/registrations/Company_registration.html', {'form': form})

def All_company_list(request):
    companies = SystemUser.objects.filter(role='company')
    return render(request, 'lists/All_company_list.html', {'companies': companies})

def Company_detail(request, pk):
    company = SystemUser.objects.get(pk=pk)
    return render(request, 'details/Company_detail.html', {'company': company})


# Managing Technicians
def Technician_registration(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            technician = form.save(commit=False)
            technician.role = 'technician'
            technician.save()
            messages.success(request, 'Your technician profile has been created, you can now login')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'forms/registrations/Technician_registration.html', {'form': form})

def All_technician_list(request):
    technicians = SystemUser.objects.filter(role='technician')
    return render(request, 'lists/All_technician_list.html', {'technicians': technicians})

def Technician_detail(request, pk):
    technician = SystemUser.objects.get(pk=pk)
    return render(request, 'details/Technician_detail.html', {'technician': technician})



# Managing Dispatchers
def Dispatcher_registration(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.role = 'dispatcher'
            form.save()
            return redirect('forms/login/login.html')
    else:
        form = UserSignUpForm()
    return render(request, 'forms/registrations/Dispatcher_registration.html', {'form': form})

def All_dispatcher_list(request):
    dispatchers = SystemUser.objects.filter(role='dispatcher')
    return render(request, 'lists/All_dispatcher_list.html', {'dispatchers': dispatchers})

def Dispatcher_detail(request, pk):
    dispatcher = SystemUser.objects.get(pk=pk)
    return render(request, 'details/Dispatcher_detail.html', {'dispatcher': dispatcher})



# Managing user profile
def Update_user_profile(request):
    if request.method == "POST":
        form = SystemUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('home')
        else:
            messages.error(request, 'You are not authorized to update this profile')
            return redirect('login')
    else:
        messages.warning(request, 'You have to be logged in to update your profile')
        form = SystemUserUpdateForm(instance=request.user)
    return render(request, 'forms/updates/User_profile_update.html', {'form': form})


# Managing user feedback form
def Feedback_registration(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your feedback has been submitted, Thank you for your feedback')
            return redirect('Feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'home.html', {'form': form})

def Feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'lists/feedback.html', {'feedbacks': feedbacks})

def Feedback_detail(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    return render(request, 'details/Feedback_detail.html', {'feedback': feedback})

def Post_feedback(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    feedback.status = 'Posted'
    feedback.save()
    messages.success(request, 'Feedback posted on home page')
    return redirect('home')


def Delete_feedback(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    feedback.delete()
    messages.success(request, 'Feedback deleted successfully')
    return redirect('Feedback_list')

def Remove_feedback(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    feedback.status = 'Removed'
    feedback.save()
    messages.success(request, 'Feedback removed from home page')
    return redirect('')
