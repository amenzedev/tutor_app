from django.shortcuts import render
from .models import Tutor

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutor_list.html', {'tutors': tutors})
