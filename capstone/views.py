from django.shortcuts import render
from .models import Artist, Sound

# Create your views here.
# from django.http import JsonResponse

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'capstone/artist_list.html', {'artists': artists})

def sound_list(request):
    sounds = Sound.objects.all()
    return render(request, 'capstone/sound_list.html', {'sounds': sounds})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'capstone/artist_detail.html', {'artist': artist})

def sound_detail(request, pk):
    sound = Sound.objects.get(id=pk)
    return render(request, 'capstone/sound_detail.html', {'sound': sound})