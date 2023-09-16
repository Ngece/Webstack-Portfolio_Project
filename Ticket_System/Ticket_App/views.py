from django.shortcuts import render, redirect
from .forms import CompanyForm, TicketForm, TechnicianForm, DispatcherForm
from .models import Company, Ticket, Technician, Dispatcher

# Create your views here.
def home(request):
    return render(request, 'home.html')


def Ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'lists/Ticket_list.html', {'tickets': tickets})

def Ticket_registration(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ticket_list')
    else:
        form = TicketForm()

    return render(request, 'registrations/Ticket_registration.html', {'form': form})
     


def Company_list(request):
    companies = Company.objects.all()
    return render(request, 'lists/Company_list.html', {'companies': companies})


def Company_registration(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Company_list')  # Redirect to the 'Company_list' view
    else:
        form = CompanyForm()
    
    return render(request, 'registrations/Company_registration.html', {'form': form})



def Technician_list(request):
    technicians = Technician.objects.all()
    return render(request, 'lists/Technician_list.html', {'technicians': technicians})

def Technician_registration(request):
    if request.method == "POST":
        form = TechnicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Technician_list')
    else:
        form = TechnicianForm()
    
    return render(request, 'registrations/Technician_registration.html', {'form': form})



def Dispatcher_list(request):
    dispatchers = Dispatcher.objects.all()
    return render(request, 'lists/Dispatcher_list.html', {'dispatchers': dispatchers})

def Dispatcher_registration(request):
    if request.method == "POST":
        form = DispatcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dispatcher_list')
    else:
        form = DispatcherForm()
    return render(request, 'registrations/Dispatcher_registration.html', {'form': form})

    #def Dispatcher_list(request):
    #return render(request, 'Dispatcher_list.html')