from django.urls import path
from . import views


#url endpoints
urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.moviehome, name="movies"),
    path("movies/details/<int:movieid>", views.details, name="details"),
    path("movies/synopsis/", views.synopsis, name="synopsis"),


]