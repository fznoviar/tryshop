from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model)

from django.contrib.auth.models import User
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            User.objects.create_user(
                username=username, email=form.cleaned_data['email'].lower(),
                password=form.cleaned_data['password'], name=form.cleaned_data['name']
            )
            # set email to lowercases because we automatically convert email to lower on registration
            new_member = authenticate(username=username, password=request.POST['password'])
            auth_login(request, new_member)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "regis.html", {
        'form': form,
    })
