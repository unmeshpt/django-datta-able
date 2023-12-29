from .models import Staff   
def user_staff(request):
    staff = {}
    if request.user.is_authenticated:
        try:
            staff['staff'] = Staff.objects.get(user=request.user)
        except Staff.DoesNotExist:
            return staff
    return staff