from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . models import Notes
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import NoteForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'notes/home.html')

def notes(request):
    context= {
        'notes' : Notes.objects.all().order_by('-date_created')
    }
    return render(request, 'notes/notes.html', context)


class addNotesView(CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/add_notes.html'
    # fields = ['note_title', 'note_content']


class NotesUpdate(UpdateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/update_notes.html'
    # fields = ['note_title', 'note_content']

class NotesDelete(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes-content')
    template_name = 'notes/delete_notes.html'
    # fields = ['note_title', 'note_content']

