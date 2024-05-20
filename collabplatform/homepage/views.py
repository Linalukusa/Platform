from django.shortcuts import render, redirect
from .models import *
import os
import csv
from django.http import HttpResponse
from .utils.separate_code_and_description import separate_code_and_description  # Update the import statement
# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def excel_processing_view(request):
    excel_file_path = os.path.join("C:\\", "Users", "lukus", "Downloads", "Platform", "collabplatform", "homepage", "files", "Non-contracted.xlsx")

    # Call the function from the imported module
    separated_data = separate_code_and_description(excel_file_path)
    
    # Write separated data to a CSV file
    output_file_path = os.path.join("C:\\", "Users", "lukus", "Downloads", "Platform", "collabplatform", "homepage", "files", "Non-contracted.csv")

    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Code', 'Description'])  # Write header
        csv_writer.writerows(separated_data)

    return HttpResponse("Data has been processed and written to the CSV file.")