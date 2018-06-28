from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse
from .utils import get_cart_items_and_total


def add_to_cart(request):
    
    #get the product we're adding
    id = request.POST['product_id']
    product = get_object_or_404(Product,pk=id)
    
    #get the current cart
    cart = request.session.get ('cart',{})
    
    #update cart
    cart[id] = cart.get(id,0)+1
    
    #save the cart back to the session
    request.session['cart'] = cart
    
    #redirect somewhere
    
    return redirect('products')
    
    
    
def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/viewcart.html", context)
    
    
def delete_item(request):
     #get the product we're adding
    id = request.POST.get('product_id')  
    
    
    #get the current cart
    cart = request.session.get('cart',{})
    
    if cart[id] > 1:
        #update cart
        cart[id] = cart.get(id,0)-1
    
    else: 
        del cart[id]
    request.session['cart'] = cart
    return redirect("view_cart")
    
    
