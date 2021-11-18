from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url= models.TextField()

    def _str_(self):
        return self.name

# class Sound(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='sounds')
#     title = models.CharField(max_length=100)
#     photo_url = models.TextField()