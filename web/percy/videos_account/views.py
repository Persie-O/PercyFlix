from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import MovieForm, EpisodeForm, SeasonForm, SeriesForm
from .models import Series, Movie, Episode, Season
import random

@login_required(login_url='login-User')
@user_passes_test(lambda u: u.is_staff)
def upload_content(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        series_form = SeriesForm(request.POST, request.FILES)
        season_form = SeasonForm(request.POST, request.FILES)
        episode_form = EpisodeForm(request.POST, request.FILES)

        if 'movie_form' in request.POST and movie_form.is_valid():
            movie_form.save()
            messages.success(request, 'Movie uploaded successfully.')
            return redirect('dashboard')  # Redirect to a success page or another view

        if 'series_form' in request.POST and series_form.is_valid():
            series_form.save()
            messages.success(request, 'Series uploaded successfully.')
            return redirect('upload_content')  # Redirect to a success page or another view
        
        if 'season_form' in request.POST and season_form.is_valid():
            season_form.save()
            messages.success(request, 'Season uploaded successfully.')
            return redirect('upload_content')

        if 'episode_form' in request.POST and episode_form.is_valid():
            episode_form.save()
            messages.success(request, 'Episode uploaded successfully.')
            return redirect('dashboard')  # Redirect to a success page or another view
        else:
            messages.error(request, 'Error: Please check the form data and try again.')

    else:
        movie_form = MovieForm()
        series_form = SeriesForm()
        season_form = SeasonForm()
        episode_form = EpisodeForm()

    context = {
        'movie_form': movie_form,
        'series_form': series_form,
        'season_form': season_form,
        'episode_form': episode_form,
    }

    return render(request, 'videos_account/upload_content.html', context)



#staff dashbord only
@login_required(login_url='login-User')
@user_passes_test(lambda u: u.is_staff)
def manage_content(request):
    return render(request, 'videos_account/manage_content.html')


@login_required(login_url='login-User')
def videos(request):
    series_list = Series.objects.all()
    movie_list = Movie.objects.all()

    # Select a random poster from either movies or series
    random_poster = None
    if series_list or movie_list:
        poster_list = list(series_list) + list(movie_list)
        random_poster = random.choice(poster_list)

        
    series_seasons_episodes = []
    
    for series in series_list:
        seasons = Season.objects.filter(series=series)
        series_data = {
            'series': series,
            'seasons': [],
        }

        for season in seasons:
            episodes = Episode.objects.filter(season=season)
            season_data = {
                'season': season,
                'episodes': episodes,
            }
            series_data['seasons'].append(season_data)

        series_seasons_episodes.append(series_data)

    
    context = {
        'series_list': series_list,
        'movie_list': movie_list,
        'series_seasons_episodes': series_seasons_episodes,
        'random_poster': random_poster,
    }
    
    return render(request, 'videos_account/videos.html', context)




@login_required(login_url='login-User')
@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    series_list = Series.objects.all()

    series_seasons_episodes = []
    
    for series in series_list:
        seasons = Season.objects.filter(series=series)
        series_data = {
            'series': series,
            'seasons': [],
        }

        for season in seasons:
            episodes = Episode.objects.filter(season=season)
            season_data = {
                'season': season,
                'episodes': episodes,
            }
            series_data['seasons'].append(season_data)

        series_seasons_episodes.append(series_data)

    movie_list = Movie.objects.all()
    
    context = {
        'series_list': series_list,
        'movie_list': movie_list,
        'series_seasons_episodes': series_seasons_episodes,
    }
    
    return render(request, 'videos_account/dashboard.html', context)










