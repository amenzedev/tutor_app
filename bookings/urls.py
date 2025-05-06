from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:tutor_id>/', views.book_tutor),
]
