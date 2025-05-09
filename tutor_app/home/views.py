from django.shortcuts import render
from accounts.models import TutorProfile

def home_view(request):
    featured_tutors = TutorProfile.objects.all().order_by('-created_at')[:3]
    return render(request, 'home/home.html', {'featured_tutors': featured_tutors})