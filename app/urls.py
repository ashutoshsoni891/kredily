from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/registerUser/', views.add_user),
    path('v1/addProduct/', views.add_product),
    path('v1/addOrder/', views.add_order),
    path('v1/orderHistory/', views.order_history),
    path('v1/getProducts/', views.get_products)
]