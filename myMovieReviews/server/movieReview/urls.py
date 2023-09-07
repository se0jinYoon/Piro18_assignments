from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('movies/create', views.movie_create),
    path("movies/<int:pk>", views.movie_detail),
    path("movies/<int:pk>/update", views.movie_update),
    path("movies/<int:pk>/delete", views.movie_delete)
]