from clients.models import *
from profiles.models import *
def active_orders(request):
    activeorders = {}
    if request.user.is_authenticated:
        try:
            activeorders['allorders'] = NewOrder.objects.select_related('user').filter(user=request.user.id)
            activeorders['completedorders'] = NewOrder.objects.select_related('user').filter(order_status="Completed")
            activeorders['cancelledorders'] = NewOrder.objects.select_related('user').filter(order_status="Cancelled")
            activeorders['activeorders'] = NewOrder.objects.select_related('user').filter(order_status="Active")
            activeorders['rejectedorders'] = NewOrder.objects.select_related('user').filter(order_status="Rejected")
            activeorders['approvedorders'] = NewOrder.objects.select_related('user').filter(order_status="Approved")
            activeorders['pendingorders'] = NewOrder.objects.select_related('user').filter(order_status="Pending")
        except NewOrder.DoesNotExist:
            return activeorders
    return activeorders