from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-form"),
    path("about", views.AboutView.as_view(), name="about")
]
