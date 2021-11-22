from django.shortcuts import render, redirect
from .models import Artist, Sound
from .forms import ArtistForm, SoundForm
from django.http import JsonResponse

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

def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'capstone/artist_form.html', {'form': form})

def sound_create(request):
    if request.method == 'POST':
        form = SoundForm(request.POST)
        if form.is_valid():
            sound = form.save()
            return redirect('sound_detail', pk=sound.pk)
    else:
        form = SoundForm()
    return render(request, 'capstone/sound_form.html', {'form': form})

def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'capstone/artist_form.html', {'form': form})

def sound_edit(request, pk):
    sound = Sound.objects.get(pk=pk)
    if request.method == "POST":
        form = SoundForm(request.POST, instance=sound)
        if form.is_valid():
            sound = form.save()
            return redirect('sound_detail', pk=sound.pk)
    else:
        form = SoundForm(instance=sound)
    return render(request, 'capstone/sound_form.html', {'form': form})

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

def sound_delete(request, pk):
    Sound.objects.get(id=pk).delete()
    return redirect('sound_list')


# def artist_list(request):
#     artists = Artist.objects.all().values('name', 'nationality', 'photo_url') # only grab some attributes from our database, else we can't serialize it.
#     artists_list = list(artists) # convert our artists to a list instead of QuerySet
#     return JsonResponse(artists_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.
