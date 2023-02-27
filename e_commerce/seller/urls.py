from django.urls import path
from . import views

app_name = "seller"

urlpatterns = [
    path('seller_home',views.seller_home, name="seller_home"),
    path('product_catelogue',views.product_catelogue,name = "product_catelogue"),
    path('add_product',views.add_product, name="add_product"),
    path('change_password', views.change_password, name="change_password"),
    path('update_stock',views.update_stock , name="update_stock"),
    path('order_history', views.order_history, name="order_history"),
    path('seller_profile',views.seller_profile, name="seller_profile"),
    path('logout',views.logout,name="logout")
]