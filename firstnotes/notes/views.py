from django.shortcuts import render
from django.http import Http404
from .models import Note

def list_notes(request):
    # Logic to list notes
    all_notes = Note.objects.all()
    return render(request, 'notes/list_notes.html', {'all_notes': all_notes})
    # If no notes are found, return an empty list

# Create your views here.

def note_details(request, note_id):
    # Logic to get details of a specific note
    try:
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/note_details.html', {'note': note})
    except Note.DoesNotExist:
        raise Http404("Note not found")
