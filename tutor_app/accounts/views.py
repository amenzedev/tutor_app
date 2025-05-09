from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, StudentProfileForm, TutorProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Please complete your profile.')
            if(user.user_type == "student"):
                return redirect('student_profile')
            else:
                return redirect('tutor_profile')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required
def student_profile(request):
    profile = request.user.student_profile
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=profile)
    return render(request, 'accounts/student_profile.html', {'form': form})


@login_required
def tutor_profile(request):
    profile = request.user.tutor_profile
    if request.method == 'POST':
        form = TutorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('tutor_profile')
    else:
        form = TutorProfileForm(instance=profile)
    return render(request, 'accounts/tutor_profile.html', {'form': form})


# @login_required
# def profile_view(request):
#     user = request.user
#     profile_instance = None
#     form_class = None
    
#     if user.user_type == 'student':
#         profile_instance = user.student_profile
#         form_class = StudentProfileForm
#     elif user.user_type == 'tutor':
#         profile_instance = user.tutor_profile
#         form_class = TutorProfileForm
#         return redirect('home')

#     if request.method == 'POST':
#         form = form_class(request.POST, instance=profile_instance)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile')
#     else:
#         form = form_class(instance=profile_instance)

#     # return render(request, f'accounts/{"student" if request.user.user_type == 'student' else "tutor"}_profile.html', {
#     #     'form': form,
#     #     'profile': profile_instance
#     # })
#     return redirect('home')
