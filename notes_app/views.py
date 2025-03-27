from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from notes_app.forms import NoteForm
from notes_app.models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})