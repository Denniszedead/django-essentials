from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('note/<int:pk>', views.NotesDetailView.as_view()),
    path('popular-notes', views.PopularNotesListView.as_view()),
]
