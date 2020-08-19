from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UseRegisterForm


def register(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created. You are now able to log in.')
            return redirect('login')
    else:
        form = UseRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# decorator to alter functionality of profile function.
# this decorator makes profile function return the login page
# if the user is not already logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')
