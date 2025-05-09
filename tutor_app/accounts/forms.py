from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, StudentProfile, TutorProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'password1', 'password2')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['bio', 'phone']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['bio', 'subjects', 'hourly_rate']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'subjects': forms.TextInput(attrs={'placeholder': 'Math, Science, English...'}),
        }