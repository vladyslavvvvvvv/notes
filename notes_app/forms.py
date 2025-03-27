from django import forms

from notes_app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'date_created',]