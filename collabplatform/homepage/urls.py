from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path( '', views.index, name ='index'),
    # path( 'about', views.about, name ='about'),
    # path('process-excel/', views.excel_processing_view, name='process_excel'),



    
] 