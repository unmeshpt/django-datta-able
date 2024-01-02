from django.shortcuts import render
from company.models import *

# Create your views here.
def new_order(request):
    products=Products.objects.all()
    services=Services.objects.all()
    context = {
    'parent': 'clients',
    'segment': 'new_order',
    'products':products,
    'services':services
    }
    return render(request, 'pages/clients/new_order.html', context)
