from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from .models import MovieReview

def movie_list(request) :
    movies = MovieReview.objects.all()
    text = request.GET.get("text")
    if text:
        movies = movies.filter(content__contains=text)
    return render(request, 'movieReview/movie_list.html', {"movies": movies})

def movie_detail(request:HttpRequest, pk, *args, **kwargs):
    movie = MovieReview.objects.all().get(id=pk)
    return render(request, "movieReview/movie_detail.html", {'movie':movie})

def movie_create(request: HttpRequest, *args, **kwargs):
    if request.method == "POST":
        MovieReview.objects.create(
            title=request.POST["title"],
            director=request.POST["director"],
            cast=request.POST["cast"],
            genre=request.POST["genre"],
            star=request.POST["star"],
            runtime=request.POST["runtime"],
            review=request.POST["review"],
            released = request.POST["released"],
        )
        return redirect("/")
    return render(request, 'movieReview/movie_create.html')

def movie_update(request: HttpRequest, pk, *args, **kwargs) :
    movie = MovieReview.objects.get(id=pk)
    if request.method == "POST":
        movie.title = request.POST["title"]
        movie.director = request.POST["director"]
        movie.cast = request.POST["cast"]
        movie.genre = request.POST["genre"]
        movie.star = request.POST["star"]
        movie.runtime = request.POST["runtime"]
        movie.review = request.POST["review"]
        movie.save()
        return redirect(f"/movies/{movie.id}")
    
    return render(request, "movieReview/movie_update.html", {"movie": movie})

def movie_delete(request: HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        movie = MovieReview.objects.get(id=pk)
        movie.delete()
    return redirect("/")