from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Plot, Transaction, Event, Resource
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, MemberForm, EventForm, PlotForm, EditPlotForm, ResourceForm, TransactionForm
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def plot_list(request):
    plots = Plot.objects.all()
    return render(request, 'plots.html', {'plots': plots})

def plot_detail(request, plot_id):
    plot = get_object_or_404(Plot, id=plot_id)
    return render(request, 'plot_detail.html', {'plot': plot})

def add_plot(request):
    if request.method == 'POST':
        form = PlotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plot_list')
    else:
        form = PlotForm()
    return render(request, 'add_plot.html', {'form': form})

def edit_plot(request, plot_id):
    plot = get_object_or_404(Plot, id=plot_id)
    if request.method == 'POST':
        form = EditPlotForm(request.POST, instance=plot)
        if form.is_valid():
            form.save()
            return redirect('plot_list')
    else:
        form = EditPlotForm(instance=plot)
    return render(request, 'edit_plot.html', {'form': form, 'plot': plot})

def delete_plot(request, plot_id):
    plot = get_object_or_404(Plot, id=plot_id)
    plot.delete()
    return redirect('plot_list')

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'member_detail.html', {'member': member})

def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_membership_fee = sum(transaction.membership_fee for transaction in transactions)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm()
    return render(request, 'transactions.html', {'transactions': transactions, 'total_membership_fee': total_membership_fee, 'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return render(request, 'delete_event.html', {'event': event})

def resources(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
    resources = Resource.objects.all()
    form = ResourceForm()

    sort_by_alphabet = request.GET.get('sort_by_alphabet')
    if sort_by_alphabet:
        resources = resources.order_by('title')

    sort_by_topic = request.GET.get('sort_by_topic')
    if sort_by_topic:
        resources = resources.order_by('topic')

    return render(request, 'resources.html', {'resources': resources, 'form': form})

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        resource.delete()
        return redirect('resources')

    return render(request, 'resource_detail.html', {'resource': resource})

def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')
    else:
        form = ResourceForm()
    return render(request, 'add_resource.html', {'form': form})





