from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, f'{username}! Account Created Successfuly, You are now able to Login')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
        return render(request, 'users/profile.html')
