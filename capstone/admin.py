from django.contrib import admin
from .models import Artist, Sound


# Register your models here.
admin.site.register(Artist)
admin.site.register(Sound)