from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from profiles.models import *
from clients.models import *

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

def order_approve(request, pk):
  order= NewOrder.objects.get(pk=pk)
  order.order_status="Approved"
  order.save()
  messages.success(request,"Order approved!!!")
  return redirect ("index")
  
def order_reject(request, pk):
  order= NewOrder.objects.get(pk=pk)
  order.order_status="Rejected"
  order.save()
  messages.success(request,"Order rejected!!!")
  return redirect ("index")

def order_pending(request, pk):
  order= NewOrder.objects.get(pk=pk)
  order.order_status="Pending"
  order.save()
  messages.success(request,"Order Pending!!!")
  return redirect ("index")

def order_cancel(request, pk):
  order= NewOrder.objects.get(pk=pk)
  order.order_status="Cancelled"
  order.save()
  messages.success(request,"Order Cancelled!!!")
  return redirect ("index")

def order_completed(request, pk):
  order= NewOrder.objects.get(pk=pk)
  order.order_status="Completed"
  order.save()
  messages.success(request,"Order Completed!!!")
  return redirect ("index")

