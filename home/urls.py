from django.urls import path

from home.views import home, authorized

urlpatterns = [
    path('home/', home),
    path('authorized/', authorized)
]
