from .views import view_cart, add_to_cart
from django.urls import path


urlpatterns = [
    path('cart/view',view_cart, name="view_cart"),
    path('cart/add',add_to_cart, name="add_to_cart"),
    
]

