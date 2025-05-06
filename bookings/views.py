from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from tutors.models import Tutor
from students.models import Student
from django.contrib.auth.decorators import login_required

@login_required
def book_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        Booking.objects.create(
            student=student,
            tutor=tutor,
            date=request.POST['date'],
            time=request.POST['time'],
            topic=request.POST['topic'],
            status='Pending'
        )
        return redirect('/')
    return render(request, 'booking_form.html', {'tutor': tutor})
