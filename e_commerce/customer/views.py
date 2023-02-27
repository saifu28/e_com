from django.shortcuts import redirect, render

from commen.models import Customer

from seller.models import Product
from customer.models import Cart
from . decorators import auth_customer
from django.db.models import F



# Create your views here.

@auth_customer
def cart(request):
    cart_data = Cart.objects.filter(customer_id=request.session['customer'])
    cart_data = Cart.objects.annotate(total = F('product__price')*F('quantity'))
    return render(request, 'customer_templates/cart.html',{'data':cart_data} )

def change_pass(request):
    if request.method == 'POST':
        c_pass = request.POST['password']
        customer = Customer.objects.get()

    customer_data = Customer.objects.get(id=request.session['customer'])

    return render(request, 'customer_templates/change_pass.html',{'data':customer_data})

def customer_home(request):
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render(request, 'customer_templates/customer_home.html',{'data':customer_data})

def customer_signup(request):
    return render(request, 'customer_templates/customer_signup.html')

def order(request):
    return render(request, 'customer_templates/order.html')

def product(request):
    product_data = Product.objects.all()
    return render(request, 'customer_templates/products.html',{'data':product_data})

def profile(request):
    msg = ''
    customer_data = Customer.objects.get(id=request.session['customer'])

    if request.method == 'POST':
        new_name = request.POST['edit_name']
        new_mail = request.POST['edit_mail']
        new_address = request.POST['edit_shipping']
        new_phone = request.POST['edit_phone']

        customer1 = Customer.objects.get(id=request.session['customer'])

        customer1 = Customer(customer_name = new_name,
                                         customer_mail = new_mail,customer_addres = new_address,
                                         customer_phone = new_phone
                                         )
        customer1.save()
        msg = 'updated'

    context ={

        'data': customer_data,
        'msg': msg
    }

        
        
    return render(request, 'customer_templates/profile.html',context)
    

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('commen:project_home')

def product_dtls(request,pid):
    msg = ''
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        quantity = request.POST['qty']
        product_exist = Cart.objects.filter(product = pid,customer = request.session['customer']).exists()
        if not product_exist:
            item = Cart(customer_id = request.session['customer'],product_id = pid,quantity = quantity)
            item.save()
        else:
            msg = 'item already added'
    context = {
        'product':product,
        'msg':msg
    }
    return render(request, 'customer_templates/product_dtls.html',context)

def remove(request,pid):
    remove_data = Cart.objects.filter(product_id=pid)
    remove_data.delete()
    return redirect('customer:cart')
