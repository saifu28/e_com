from django.shortcuts import render,redirect

from commen.models import Seller
from seller.models import Product



# Create your views here.

def seller_home(request):

    seller_data = Seller.objects.get(id=request.session['seller'])

    return render(request, 'seller_templates/seller_home.html',{'data':seller_data})

def product_catelogue(request):
    product_data = Product.objects.filter(seller_id=request.session['seller'])
    return render(request, 'seller_templates/product_catelogue.html',{'p_data':product_data})

def add_product(request):
    msg =''
    if request.method == 'POST':

        p_id = request.POST['product_id']
        p_name = request.POST['product_name']
        p_discription = request.POST['discription']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.FILES['image']

        add_product = Product(
        seller_id = request.session['seller'],
        product_id = p_id,
        product_name = p_name,
        discription = p_discription,
        stock = stock,
        price = price,
        image = image

        )
        add_product.save()
        msg = 'add product successfull'

    return render(request, 'seller_templates/add_product.html',{'mag':msg})

def change_password(request):
    return render(request, 'seller_templates/change_password.html')

def update_stock(request):
    return render(request, 'seller_templates/update_stock.html')

def order_history(request):
    return render(request, 'seller_templates/order_history.html')

def seller_profile(request):
    seller_data = Seller.objects.get(id=request.session['seller'])

    return render(request, 'seller_templates/seller_profile.html',{'data':seller_data})

def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('commen:project_home')
