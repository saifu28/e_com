from django.http import JsonResponse
from django.shortcuts import render,redirect

# class importing here
from commen.models import Customer, Seller

# user pass auto genarationg bilting function
# to send the genarated pass in email 
from django.core.mail import send_mail


from django.conf import settings

import random

# Create your views here.

def project_home(request):
    return render(request, 'commen_templates/project_home.html')



def customer_sign(request):
    # get values by input area and store the values in a variable
    if request.method == 'POST':
        customer_name = request.POST['db_name']
        customer_phone = request.POST['db_phone']
        customer_mail = request.POST['db_mail']
        customer_image = request.FILES['db_image']
        customer_password = request.POST['db_password']
        customer_addres = request.POST['db_addres']
        # stored veriable values assign the class veriable(db column) db veriale = created veriable
        new_customer = Customer(
            customer_name = customer_name,
            customer_phone = customer_phone,
            customer_mail= customer_mail,
            customer_image = customer_image,
            customer_password= customer_password,
            customer_addres= customer_addres
        )     
        # save the all values in a new veriable  
        new_customer.save()

    
    return render(request, 'commen_templates/customer_sign.html')



def customer_login(request):
    # exaption message
    msg = ''
    # customer login time get the values mail&pass and store the values in veriable
    if request.method == 'POST':
        cust_mail = request.POST['db_mail']
        cust_password = request.POST['db_password']
        # stored values cross check by the clss veriable(checked with db values)
        try:
            customer = Customer.objects.get(customer_mail = cust_mail,customer_password = cust_password)
            request.session['customer'] = customer.id
            # if conditon match return work 
            return redirect('customer:customer_home')
        # condition false msg return(exaption)
        except:
            msg = 'invalid password or mail'

    return render(request, 'commen_templates/customer_login.html',{'msg':msg})




def seller_sign(request):
    if request.method == 'POST':
        fname = request.POST['s_name']
        phone = request.POST['s_phone']
        mail = request.POST['s_mail']
        cname = request.POST['s_cname']
        image = request.FILES['s_image']
        acnumber = request.POST['s_acnumber']
        ifsc = request.POST['s_ifsc']
        account_holder = request.POST['s_acholdername']
        branch = request.POST['s_branch']
        address = request.POST['s_address']
        s_username = random.randint(1111,9999)
        s_pass = 'sel-' + fname.lower() + str(s_username)
        message = 'Hii your username is :' + str(s_username) + 'temporary password is ' + s_pass 

        new_seller = Seller(
            seller_first_name = fname,
            phone = phone,
            mail = mail, 
            company_name = cname,
            image = image,
            ac_number = acnumber,
            ifsc = ifsc,
            account_holder = account_holder,
            branch = branch,
            address = address,
            user_name = s_username,
            password = s_pass
        )
        send_mail(
            'user name and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [mail],
            fail_silently = False
        )
        new_seller.save()

    return render(request, 'commen_templates/seller_sign.html')




def seller_login(request):
    msg = ''
    if request.method == 'POST':
        seller_username = request.POST['s_username']
        seller_password = request.POST['s_password']
        try:
            seller = Seller.objects.get(user_name = seller_username,password = seller_password)
            request.session['seller'] = seller.id
            return redirect('seller:seller_home')

        except:
            msg = 'invalid pass or username'

    return render(request, 'commen_templates/seller_login.html',{'msg':msg})

def email_exist(request):
    
    email = request.POST['email']
    status = Customer.objects.filter(customer_mail = email).exists()
    return JsonResponse({'status':status})