from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *
from profiles.models import Profile

@login_required(login_url='/accounts/login/')
def index(request):
  if request.user is not None:
    profile = Profile.objects.filter(user=request.user).first()
  else:
    profile=None
  context = {
    'segment'  : 'index',
    'profile' : profile
  }
  
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)
