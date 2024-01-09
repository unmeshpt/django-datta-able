from .models import Profile  
def user_profile(request):
    profile = {}
    if request.user.is_authenticated:
        try:
            profile['profile'] = Profile.objects.select_related('user').filter(user=request.user).first()
        except Profile.DoesNotExist:
            return profile
    return profile