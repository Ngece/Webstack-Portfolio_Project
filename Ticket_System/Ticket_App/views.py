from django.shortcuts import render, redirect
from .models import Company, Ticket, Technician, Dispatcher
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CompanyRegistrationForm, TechnicianRegistrationForm, DispatcherRegistrationForm, TicketCreationForm



# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


class CompanyRegistrationView(CreateView):
    model = Company
    form_class = CompanyRegistrationForm
    template_name = 'forms/registration/company_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
#def company_register(request):
#    return render(request, 'forms/registration/company_register.html', {})

def company_detail(request):
    return render(request, 'details/company_detail.html', {})

def company_update(request):
    return render(request, 'forms/update/company_update.html', {})


def create_ticket(request):
    if request.method == 'POST':
        form = TicketCreationForm(request.POST)
        if form.is_valid():
            ticket = form.save()

            if request.user.is_company:
                return redirect('user_tickets')
            elif request.user.is_technician:
                return redirect('user_tickets')
            else:
                return redirect('ticket_detail', ticket_id=ticket.id)  # Redirect to the ticket detail page for dispatchers

    else:
        form = TicketCreationForm()

    return render(request, 'ticket_create.html', {'form': form})


def user_tickets(request):
    if request.user.is_company:
        tickets = Ticket.objects.filter(ticket_company=request.user)
    elif request.user.is_technician:
        tickets = Ticket.objects.filter(ticket_technician=request.user)
    else:
        tickets = Ticket.objects.all()  # For dispatchers, show all tickets
    return render(request, 'user_tickets.html', {'tickets': tickets})


def ticket_detail(request):
    return render(request, 'details/ticket_detail.html', {})

def ticket_update(request):
    return render(request, 'forms/update/ticket_update.html', {})



class TechnicianRegistrationView(CreateView):
    model = Company
    form_class = TechnicianRegistrationForm
    template_name = 'forms/registration/technician_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
#def technician_create(request):
#    return render(request, 'forms/registration/technician_create.html', {})

def technician_detail(request):
    return render(request, 'details/technician_detail.html', {})

def technician_update(request):
    return render(request, 'forms/update/technician_update.html', {})




class DisptcherRegistrationView(CreateView):
    model = Company
    form_class = DispatcherRegistrationForm
    template_name = 'forms/registration/dispatcher_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
#def dispatcher_create(request):
#    return render(request, 'forms/registration/dispatcher_create.html', {})

def dispatcher_detail(request):
    return render(request, 'details/dispatcher_detail.html', {})

def dispatcher_update(request):
    return render(request, 'forms/update/dispatcher_update.html', {})
