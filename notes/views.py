from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . models import Notes
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'notes/home.html')

def notes(request):
    context= {
        'notes' : Notes.objects.all()
    }
    return render(request, 'notes/notes.html', context)


class addNotesView(CreateView):
    model = Notes
    template_name = 'notes/add_notes.html'
    fields = ['note_title', 'note_content']


