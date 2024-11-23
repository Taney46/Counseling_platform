from django import forms
from .models import Session
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class BookingForm(forms.ModelForm):
    counselor = forms.ModelChoiceField(
        queryset=User.objects.filter(profile__is_counselor=True),
        empty_label="Select a counselor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = Session
        fields = ['counselor', 'date', 'notes']  # Use 'notes' instead of 'description'

