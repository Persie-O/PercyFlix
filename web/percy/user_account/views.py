# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup_view(request):
    form = SignUpForm()  # Create an instance of the form

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Account successfully created for ' + username)
        return redirect('login-User')

    context = {'form':form}  # Assign the form to the context
    return render(request, 'user_account/register.html', context)


@csrf_protect
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("Authenticated:", user)

        if user is not None:
                login(request, user)
                if user.is_staff:
                    messages.success(request, 'Logged in successfully as staff')
                    return redirect('dashboard')  # Redirect to staff dashboard
                else:
                    messages.success(request, 'Logged in successfully as user')
                    return redirect('videos')
                
        else:
            messages.info(request, 'Incorect details')
    context = {}
    return render(request, 'user_account/login.html',context)

#handles user logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully. We\'ll miss you')
    return redirect('login-User')  # Redirect to the login page



