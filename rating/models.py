from django.db import models

class Movie(models.Model):
	name = models.CharField(max_length=255, default="", db_index=True)
	director = models.CharField(max_length=255, default="", blank=True)
	popularity = models.FloatField(default=0.0)
	imdb_score = models.FloatField(default=0.0)
	

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='genre', unique=False)
    name = models.CharField(max_length=255, default="", db_index=True)