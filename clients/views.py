from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from company.models import *
from .models import *
from api.serializers import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def orders(request):
    all_oders = NewOrder.objects.filter(user=request.user).order_by('order_no')
    order_items= OrderItem.objects.all()
    context = {
        'parent': 'clients', 'segment': 'sent_orders', 
        'all_oders':all_oders, 'order_items':order_items,
    }

    return render(request, 'pages/clients/sent.html', context)


@login_required(login_url='/accounts/login/')
def add_product(request):
    if request.method == 'POST':
       orderitem =OrderItem()
       orderitem.new_order=NewOrder.objects.get(user=request.user, order_status='New')
       orderitem.item = request.POST['item']
       orderitem.description = request.POST['description']
       orderitem.quantity = request.POST['quantity']
       orderitem.save()
       # messages.success(request,"Item Added successfully")
       return redirect('new_order')

@login_required(login_url='/accounts/login/')
def create_order(request):

    neworder = NewOrder.objects.filter(user=request.user, order_status='New').first()
    order_items= OrderItem.objects.filter(new_order__order_no=neworder.order_no)

    if request.method == 'POST':
        if  not order_items.count() == 0 :
            neworder.project_name = request.POST['project_name']
            neworder.deadline = request.POST['deadline']
            if request.FILES.get('assets'):
                neworder.assets =request.FILES['assets']
            neworder.order_status= 'Active'
            neworder.save()
            messages.success(request,"Order sent successfully")
            return redirect('new_order')
        else:
           messages.warning(request,"No item added yet!!!")
           return redirect('new_order')
 

@login_required(login_url='/accounts/login/')
def new_order(request):
    neworder = NewOrder.objects.filter(user=request.user, order_status='New').first()
    if (neworder is None):
        neworder=NewOrder()  
        neworder.user=request.user
        neworder.order_no = generate_order_number()
        neworder.project_name = ""
        neworder.deadline = (datetime.now() + timedelta(days = 5)).date().isoformat()
        neworder.order_status= 'New'
        neworder.save()
        return redirect('new_order')
    
    order_items= OrderItem.objects.filter(new_order__order_no=neworder.order_no)
    products=Products.objects.all()
    services=Services.objects.all()
   
    context = {
        'parent': 'clients', 'segment': 'new_order', 
        'products':products, 'services':services, 'order_items':order_items,
        'neworder':neworder
    }

    return render(request, 'pages/clients/new_order.html', context)


@login_required (login_url='/accounts/login/')
def delete_addeditem(request, id):
    instance = get_object_or_404(OrderItem, id=id)
    instance.delete()
    messages.success(request,"Item deleted successfully")
    return redirect('new_order')

@login_required (login_url='/accounts/login/')
def del_order(request, id):
    instance = get_object_or_404(NewOrder, id=id)
    instance.delete()
    messages.success(request,"Order deleted successfully")
    return redirect('orders')

@login_required (login_url='/accounts/login/')
def view_order(request, id):
    order = NewOrder.objects.get(pk=id)
    order_items= OrderItem.objects.filter(new_order__order_no=order.order_no).order_by('id')
    context = {
        'order_items':order_items,   
    }
    return render(request, 'pages/clients/sent.html', context)