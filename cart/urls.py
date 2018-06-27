from .views import view_cart, add_to_cart ,delete_item
from django.urls import path


urlpatterns = [
    path('cart/view',view_cart, name="view_cart"),
    path('cart/add',add_to_cart, name="add_to_cart"),
    path('cart/delete',delete_item, name="delete_item")
 
]

