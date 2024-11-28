from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=255)                                        # Título principal en inglés
    #cover_image = models.ImageField(upload_to="anime_covers/")                      # Imagen de portada
    title_jp = models.CharField(max_length=255)                                     # Título en japonés
    title_romaji = models.CharField(max_length=255)                                 # Título en romaji (transliteración al alfabeto latino)
    description = models.TextField()                                                # Descripción del anime
    date_aired = models.DateField()                                                 # Fecha en que el anime se emitió por primera vez
    views = models.PositiveIntegerField()                                           # Número de vistas totales del anime
    score = models.FloatField()                                                     # Puntuación promedio del anime
    duration = models.DurationField()                                               # Duración del anime (puede usarse para episodios o películas)

    genres = models.ManyToManyField('Genre')                                        # Relación de muchos a muchos con géneros
    anime_type = models.ForeignKey('AnimeType', on_delete=models.CASCADE)           # Relación con la tabla de tipos (movie, TV series)
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE)                  # Relación con la tabla de estudios
    status = models.ForeignKey('Status', on_delete=models.CASCADE)                  # Relación con la tabla de estados (airing, finalizado, etc.)
    quality = models.ForeignKey('Quality', on_delete=models.CASCADE)                # Relación con la tabla de calidad (ej: HD, FullHD, 4K)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    name = models.CharField(max_length=50)  # Ejemplo: Action, Comedy, Drama

class AnimeType(models.Model):
    name = models.CharField(max_length=50)  # Ejemplo: Movie, TV Series, OVA

class Studio(models.Model):
    name = models.CharField(max_length=100)  # Nombre del estudio (ejemplo: Kyoto Animation, Madhouse)
    country = models.CharField(max_length=50, blank=True, null=True)  # País del estudio (opcional)
    established_year = models.PositiveIntegerField(blank=True, null=True)  # Año de fundación (opcional)

class Status(models.Model):
    name = models.CharField(max_length=50)  # Ejemplo: Airing, Completed, Cancelled

class Quality(models.Model):
    name = models.CharField(max_length=50)  # Ejemplo: SD, HD, FullHD, 4K

