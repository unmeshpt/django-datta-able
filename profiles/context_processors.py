from .models import Profile  
def user_profile(request):
    profile = {}
    if request.user.is_authenticated:
        try:
            profile['profile'] = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return profile
    return profile