from django.views.generic import CreateView, ListView, DetailView

from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'

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
