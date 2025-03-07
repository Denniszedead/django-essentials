from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('note/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'),
    path('note/public/<int:pk>', views.PublicNotesDetailView.as_view(), name='notes.public'),
    path('popular-notes', views.PopularNotesListView.as_view()),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
    path('note/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('note/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('note/<int:pk>/add_like', views.add_like_view, name='notes.add_like'),
    path('note/<int:pk>/toggle_isPublic', views.toggle_isPublic_view, name='notes.toggle_is_public'),
]
