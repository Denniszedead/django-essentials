from django.urls import path

from . import views
from .views import LogoutInterfaceView

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
    path('login/', views.LoginInterfaceView.as_view()),
    path('logout/', LogoutInterfaceView.as_view()),
]
