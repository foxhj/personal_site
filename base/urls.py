from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('submit-message/', views.submit_message, name='submit-message'),
    path('download-resume/', views.download_resume, name='download-resume')
]