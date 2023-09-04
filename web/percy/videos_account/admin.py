from django.contrib import admin
from .models import Movie, Series, Season, Episode
from .forms import MovieForm, SeriesForm, SeasonForm, EpisodeForm

class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

class SeriesAdmin(admin.ModelAdmin):
    form = SeriesForm

class SeasonAdmin(admin.ModelAdmin):
    form = SeasonForm

class EpisodeAdmin(admin.ModelAdmin):
    form = EpisodeForm

admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)







