from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    cast = models.TextField()
    trailer = models.FileField(upload_to='trailers/movies/')
    video_file = models.FileField(upload_to='videos/movies/')
    poster_path = models.ImageField(upload_to='posters/movies/', blank=True, null=True)

    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    poster_path = models.ImageField(upload_to='posters/series/', blank=True, null=True)

    def __str__(self):
        return self.title

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    season_number = models.PositiveIntegerField()
    description = models.TextField()
    cast = models.TextField()
    trailer = models.FileField(upload_to='trailers/series/seasons/')
    release_date = models.DateField()
    
    def __str__(self):
        return f"{self.series.title} - S{self.season_number}"

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    episode_number = models.PositiveIntegerField()
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/series/seasons/')
    release_date = models.DateField()
    
    def __str__(self):
        return f"S{self.season.season_number}E{self.episode_number}: {self.title}"








