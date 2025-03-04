from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.ListView.as_view()),
    path('notes/<int:pk>', views.detail),
]
