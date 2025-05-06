from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from students.models import Student
from tutors.models import Tutor

class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TutorRegisterForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, label='Bio')
    subjects = forms.CharField(max_length=255)
    hourly_rate = forms.DecimalField(decimal_places=2)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
