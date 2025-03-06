from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .forms import NotesForm
from .models import Notes


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class PopularNotesListView(ListView):
    queryset = Notes.objects.filter(likes__gt=1)
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
