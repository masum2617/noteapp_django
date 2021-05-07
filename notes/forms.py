from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    #modelForm allows us to create form model
    class Meta:
        model = Notes
        fields = ['note_title', 'note_content']
        widgets = {
            'note_title' : forms.TextInput(attrs={'class': 'form-control'}),
            'note_content' : forms.Textarea(attrs={'class': 'form-control'}),
        }