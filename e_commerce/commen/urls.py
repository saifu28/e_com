from django.urls import path
from . import views

app_name = 'commen'

urlpatterns = [
    path('project_home', views.project_home, name='project_home'),
    path('customer_sign', views.customer_sign, name='customer_sign'),
    path('customer_login', views.customer_login, name="customer_login"),
    path('seller_sign', views.seller_sign, name="seller_sign"),
    path('seller_login', views.seller_login, name='seller_login'),
    path('email_exist',views.email_exist,name='email_exist')
]