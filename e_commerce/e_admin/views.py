from django.shortcuts import render

# Create your views here.

def e_admin_home(request):
    return render(request, 'e_admin_templates/e_admin_home.html')

def approve_seller(request):
    return render(request, 'e_admin_templates/approve_seller.html')

def view_seller(request):
    return render(request, 'e_admin_templates/view_seller.html')

def view_costumer(request):
    return render(request, 'e_admin_templates/view_costumer.html')

def admin_login(request):
    return render(request, 'e_admin_templates/admin_login.html')