from django.shortcuts import render

# Create your views here.
def update_profile(request, user):

    context = {
    'segment': 'profile',
    }
    return render(request, 'pages/users/profile.html', context)