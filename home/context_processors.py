from clients.models import *
from profiles.models import *
def active_orders(request):
    activeorders = {}
    if request.user.is_authenticated:
        try:
            activeorders['activeorders'] = NewOrder.objects.select_related('user').filter(order_status="Active")
        except NewOrder.DoesNotExist:
            return activeorders
    return activeorders