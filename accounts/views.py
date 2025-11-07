from django.shortcuts import render, redirect
from .forms import SignupForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail



# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                "Welcome to Your Account!",
                "Your account has been successfully created in Lavrix.\nEnjoy your experience!",
                None,
                [user.email],
                fail_silently=False,
            )
            messages.success(request, "Account created successfully.")
            return redirect('accounts:login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()

    return render(request, 'account_app/signup.html', {'form': form})




def user_login(request):
    # fix added here
    if request.user.is_authenticated and not messages.get_messages(request):
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'account_app/login.html', {'form': form})





@never_cache
@login_required
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have been logged out successfully.")
    return redirect('accounts:login')


