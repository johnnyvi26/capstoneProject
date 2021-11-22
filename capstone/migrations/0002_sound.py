# Generated by Django 3.2.9 on 2021-11-18 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='not song title', max_length=100)),
                ('album', models.CharField(default='no album title', max_length=100)),
                ('preview_url', models.CharField(max_length=200, null=True)),
                ('photo_url', models.TextField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sounds', to='capstone.artist')),
            ],
        ),
    ]
