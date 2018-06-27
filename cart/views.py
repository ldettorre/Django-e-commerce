from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse


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
    
    
    
def view_cart(request):
    
    cart = request.session.get('cart',{})
    
    cart_total = 0
    cart_items = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)
        quantity= cart[p]
        
        cart_item={
            'product': product,
            'quantity': quantity,
            'sub_total': product.price * quantity
        }
        
        cart_items.append(cart_item)
        
        cart_total += cart_item['sub_total']
        
    return render (request,"cart/viewcart.html", {'cart_items':cart_items,'total':cart_total })
    
    
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
    
    
