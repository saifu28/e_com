from django.urls import path
from . import views

app_name = 'e_admin'

urlpatterns = [
    path('e_admin_home',views.e_admin_home, name = "e_admin_home"),
    path('approve_seller',views.approve_seller, name="approve_seller"),
    path('view_seller',views.view_seller, name="view_seller"),
    path('view_costumer',views.view_costumer,name="view_costumer"),
    path('admin_login',views.admin_login, name="admin_login")
]