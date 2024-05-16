from django.shortcuts import render, redirect
# like flash in flask
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# form to register
def register(request):
    # the form is already created by django we just import it
    if request.method == 'POST':
        # save in the db
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # this will save the data from the form into the db
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') #after signing up they will be redirected to login
    else:
        # if it is a GET create a new form (basically every time the page is loaded)
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    # this is handling the update, so if the user updates their profile this will handle the request
    if request.method == 'POST':
        # collecting the data from the form
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, 
                                         request.FILES, 
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


    else:
        # this will fill the form with the already existing information
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)