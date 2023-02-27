from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('cart',views.cart,name="cart"),
    path('change_pass',views.change_pass,name="change_pass"),
    path('customer_home',views.customer_home,name="customer_home"),
    path('customer_signup',views.customer_signup,name="customer_signup"),
    path('order',views.order,name="order"),
    path('product',views.product,name="product"),
    path('profile',views.profile,name="profile"),
    path('logout',views.logout,name="logout"),
    path('product_dtls/ <int:pid>',views.product_dtls,name="product_dtls"),
    path('remove/ <int:pid>',views.remove,name="remove")
    
]