from django.shortcuts import render, redirect
from .forms import UserCreationForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Profile, Session
from .models import Counselor


def homepage(request):
    return render(request, 'core/homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'core/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    next_page = '/dashboard'  # Redirect to dashboard after login

@login_required
def dashboard(request):
    user = request.user
    try:
        profile = user.profile  # This will raise an error if the profile does not exist
    except Profile.DoesNotExist:
        profile = None
    
    sessions = Session.objects.filter(user=user, status='upcoming').order_by('date')

    context = {
        'user': user,
        'profile': profile,
        'sessions': sessions,
    }

    return render(request, 'core/dashboard.html', context)

@login_required
def book_session(request):
    counselors = Profile.objects.filter(is_counselor=True)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user  # Assign the current user to the session
            session.save()
            return redirect('dashboard')  # Redirect to the dashboard after booking
    else:
        form = BookingForm()
    
    return render(request, 'core/book_session.html', {'form': form, 'counselors': counselors})


def counselor_list(request):
    counselors = Counselor.objects.all()
    return render(request, 'core/counselor_list.html', {'counselors': counselors})

