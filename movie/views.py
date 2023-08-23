from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
from .models import Premieres

# Create your views here.
def home(request):
    #return render(request, 'home.html', {'name': 'Cristian Camilo Cardenas Mogollon'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    
    premieres = Premieres.objects.all()

    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies, 'premieres': premieres})
def about(request):
    return render(request, 'about.html')