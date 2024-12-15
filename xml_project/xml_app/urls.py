from django.urls import path
from . import views

urlpatterns = [
    path('download/', views.download_xml, name='download_xml'),
]
