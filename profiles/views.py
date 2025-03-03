from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def update_profile(request):
    if  request.method == 'POST': 
        user=User.objects.get(username=request.user)
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()
    
        profile=Profile.objects.filter(user=request.user).first()
        if (profile is None):
            profile=Profile()
        profile.user = request.user
        profile.house_no = request.POST['house_no']
        profile.street = request.POST['street']
        profile.city = request.POST['city']
        profile.state = request.POST['state']
        profile.country = request.POST['country']
        profile.zipcode = request.POST['zipcode']
        profile.phone = request.POST['phone']
        profile.gender=request.POST['gender']
        profile.dob=request.POST['dob']
        profile.is_admin=False
        profile.bio = request.POST['bio'] 
        if request.FILES.get('profileimg'):
                profile.profileimg =request.FILES['profileimg']
        profile.save()
        return redirect('profile')
    else:
        profile= Profile.objects.filter(user=request.user).first()
        return render(request, 'pages/users/profile.html', {'profile':profile})
        