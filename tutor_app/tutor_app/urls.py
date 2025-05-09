"""
URL configuration for tutor_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import register, user_login, user_logout, student_profile, tutor_profile
from home.views import home_view
from tutors.views import TutorListView, TutorDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tutors/', TutorListView, name='tutor_list'),
    path('tutors/<str:username>/', TutorDetailView, name='tutor_detail'),
    path('profile/student/', student_profile, name='student_profile'),
    path('profile/tutor/', tutor_profile, name='tutor_profile'),
    path('<path:anything>', home_view, name='home'),
]
