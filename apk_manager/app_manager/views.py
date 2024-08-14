from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import App
from .forms import AppForm

def register(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('login')
  
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def app_list(request):
    apps = App.objects.filter(uploaded_by=request.user)
    return render(request, 'app_manager/app_list.html', {'apps': apps})

@login_required
def app_add(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.uploaded_by = request.user
            app.save()
            return redirect('app_list')
    else:
        form = AppForm()
    return render(request, 'app_manager/app_add.html', {'form': form})

@login_required
def app_update(request, app_id):
    app = get_object_or_404(App, id=app_id, uploaded_by=request.user)
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            form.save()
            return redirect('app_list')
    else:
        form = AppForm(instance=app)
    return render(request, 'app_manager/app_update.html', {'form': form})

@login_required
def app_delete(request, app_id):
    app = get_object_or_404(App, id=app_id, uploaded_by=request.user)
    if request.method == 'POST':
        app.delete()
        return redirect('app_list')
    return render(request, 'app_manager/app_delete.html', {'app': app})

