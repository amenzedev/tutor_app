from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, TutorRegisterForm
from .models import Student
from tutors.models import Tutor
from django.contrib.auth.models import User

def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'student_register.html', {'form': form})


def tutor_register(request):
    if request.method == 'POST':
        form = TutorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Tutor.objects.create(
                user=user,
                bio=form.cleaned_data['bio'],
                subjects=form.cleaned_data['subjects'],
                hourly_rate=form.cleaned_data['hourly_rate']
            )
            return redirect('login')
    else:
        form = TutorRegisterForm()
    return render(request, 'tutor_register.html', {'form': form})
