from django.urls import path
from . import views

urlpatterns = [
    path('smart/', views.list_notes, name='list_notes'),
    path('smart/<int:note_id>/', views.note_details, name='note_details'),
    # You can add more URL patterns here as needed
]