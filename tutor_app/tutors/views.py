from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from accounts.models import TutorProfile
from django.shortcuts import render


def TutorListView(request):
    tutors = TutorProfile.objects.order_by("created_at")

    return render(request, 'tutor_list.html', {'tutors': tutors[:10]})

def TutorDetailView(request, username):
    # Get the CustomUser object with the given username
    custom_tutor = get_object_or_404(CustomUser, username=username)
    # Get the User object related to that CustomUser (if needed)
    tutor = get_object_or_404(TutorProfile, user=custom_tutor)
    # Pass 'user' to the template context
    return render(request, 'tutor_detail.html', {'tutor': tutor})