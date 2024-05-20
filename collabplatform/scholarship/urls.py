from django.urls import path
from . import views

urlpatterns = [
    path( 'about', views.match_students_to_scholarships, name ='about'),



]