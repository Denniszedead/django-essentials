from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class PopularNotesListView(ListView):
    queryset = Notes.objects.filter(likes__gt=1)
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()

        return HttpResponseRedirect(
            reverse('notes.detail', args=(pk, ))
        )
    raise Http404