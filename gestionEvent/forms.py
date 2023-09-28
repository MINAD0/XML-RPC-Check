from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type', 'date', 'time', 'location', 'catering_options', 'category','image','price']


class RestaurationForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs
        fields = ['name', 'contact_info', 'services_offered']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password'
    }))


class ImageUploadForm(forms.Form):
    image = forms.ImageField(required=False)
    
class CustomEditProfileForm(UserChangeForm):
    new_email = forms.EmailField(required=False, label='New Email Address')
    new_first_name = forms.CharField(max_length=30, required=False, label='New First Name')
    new_last_name = forms.CharField(max_length=30, required=False, label='New Last Name')
    
    class Meta:
        model = UserProfile
        fields = ['new_email', 'new_first_name', 'new_last_name']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['event', 'user', 'reservation_date']

