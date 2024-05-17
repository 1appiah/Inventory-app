from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Product, Order
from . forms import ProductForm, OrderForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.staff = request.user
            form.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'form':form
    }
    return render(request,'dashboard/index.html', context)

#---staff
@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {'workers': workers,}
    return render(request,'dashboard/staff.html', context)

#--- product
@login_required(login_url='user-login')
def product(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(category__icontains=q))
        items = Product.objects.filter(multiple_q)
        #items = Product.objects.filter(name__icontains=q)
    else:
    #product.objects.raw*(--sql inside) --- allows you to write an sql query
        items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            return redirect('dashboard-product')
    else:
        form = ProductForm()    
    context = {
        'items':items,
        'form':form,
    }
    return render(request,'dashboard/product.html', context)
#---order
@login_required(login_url='user-login')
def order(request):
        
    orders = Order.objects.all().order_by('-id')
    context={
        'orders':orders
    }
    return render(request,'dashboard/order.html', context)
#--- delete
@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {}
    return render(request,'dashboard/deletepro.html', context)
#----product update
@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)    
    context = {'form':form}
    return render(request,'dashboard/updatepro.html', context)

#---staff detail page
@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id = pk)
    context = {
        'workers':workers,
    }
    return render(request,'dashboard/staff_detail.html', context)


