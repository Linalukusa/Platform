from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import get_list_or_404
from .models import Scholarship
from .utils import gale_shapley_match_students_to_scholarships
from .models import  Scholarship
from authentication.models import StudentProfile




def match_students_to_scholarships(request):
    students = get_list_or_404(StudentProfile.objects.all())
    scholarships = get_list_or_404(Scholarship.objects.all())

    matching_result = gale_shapley_match_students_to_scholarships(students, scholarships)
    
    # Print matching scholarships for debugging
    for student, scholarships in matching_result.items():
        print(f"Student: {student}, Matching Scholarships: {[scholarship.title for scholarship in scholarships]}")

    return render(request, 'scholarship/matching_result.html', {'matching_result': matching_result})




