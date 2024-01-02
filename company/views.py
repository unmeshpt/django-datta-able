from django.shortcuts import render

# Create your views here.
def add_services(request):
    context = {
        'parent': 'company',
        'segment': 'add_new_services'
    }
    return render(request, 'pages/company/add_services.html',context)