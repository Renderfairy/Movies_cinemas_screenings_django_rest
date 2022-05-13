from django.db import models
from movielist import models as m_list


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(m_list.Movie,  through="Screening")


class Screening(models.Model):
    movie = models.ForeignKey(m_list.Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    date = models.DateField()
