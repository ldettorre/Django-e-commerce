from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from products.models import Product

def get_cart(request):
    return HttpResponse("This is your cart")

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
    
    
    return HttpResponse(cart[id])