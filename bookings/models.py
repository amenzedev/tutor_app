from django.db import models
from students.models import Student
from tutors.models import Tutor

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed')
    ])

    def __str__(self):
        return f"{self.student.user.username} -> {self.tutor.user.username} on {self.date}"
