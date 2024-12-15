from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

@login_required
def download_xml(request):
    # Път до XML файла
    file_path = os.path.join(os.path.dirname(__file__), 'library.xml')

    # Четене на файла и изпращане като отговор
    with open(file_path, 'r', encoding='utf-8') as file:
        response = HttpResponse(file.read(), content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="library.xml"'
        return response
