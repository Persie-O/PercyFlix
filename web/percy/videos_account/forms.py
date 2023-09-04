from django import forms
from .models import Movie, Series, Season, Episode

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = '__all__'

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'



class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'

