from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from company.models import *
from .models import *

def create_ordernumber():
    current_year = datetime.now().year
    total_order = LastOrderNo.objects.count()
    new_order_no=total_order + 1
    order_no = f'{'ORD-' + str(current_year)[-2:]}/{str(new_order_no).zfill(3)}'
    return order_no

# Create your views here.
    
@login_required(login_url='/accounts/login/')
def add_product(request):
    order_no = create_ordernumber()
    if request.method == 'POST':
       orderitem =OrderItem()
       orderitem.new_order=NewOrder.objects.get(order_no=order_no)
       orderitem.item = request.POST['item']
       orderitem.description = request.POST['description']
       orderitem.quantity = request.POST['quantity']
       orderitem.save()
       messages.success(request,"Item Added successfully")
       return redirect('new_order')
    
    # order_items= OrderItem.objects.filter(new_order__order_no=order_no)
    # products=Products.objects.all()
    # services=Services.objects.all()
    # context = {
    #     'parent': 'clients', 'segment': 'new_order',
    #     'oder_no':order_no, 'products':products,
    #     'services':services, 'order_items':order_items,
    # }
    # return render(request, 'pages/clients/new_order.html', context)

@login_required(login_url='/accounts/login/')
def create_order(request):
    products=Products.objects.all()
    services=Services.objects.all()
    context = {
    'parent': 'clients',
    'segment': 'new_order',
    'products':products,
    'services':services
    }
    return render(request, 'pages/clients/new_order.html', context)

@login_required(login_url='/accounts/login/')
def new_order(request):
    order_no = create_ordernumber()
    neworder = NewOrder.objects.get(order_no=order_no, order_status='New' )
    
    if request.method == 'POST':
        neworder.user=request.user
        neworder.order_no = order_no
        neworder.project_name = request.POST['project_name']
        neworder.deadline = request.POST['deadline']
        neworder.order_status= 'Active'
        neworder.save()

        lastorderno=LastOrderNo()
        lastorderno.order_no=order_no
        lastorderno.save()
        
        return redirect('new_order')
    
    if  neworder is None:
        neworder=NewOrder()  
        neworder.user=request.user
        neworder.order_no = order_no
        neworder.project_name = ""
        neworder.deadline = (datetime.now() + timedelta(days = 5)).date().isoformat()
        neworder.order_status= 'New'
        neworder.save()
        return redirect('new_order')
    
   
    

    order_items= OrderItem.objects.filter(new_order__order_no=order_no)
    products=Products.objects.all()
    services=Services.objects.all()
   
    context = {
    'parent': 'clients', 'segment': 'new_order', 'oder_no':order_no,
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