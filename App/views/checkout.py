from django.shortcuts import render, redirect

from App.models.customer import Customer
from django.views import View

from App.models.product import Product
from App.models.orders import Order


class CheckOut(View):
    def post(self, request):
        
        address             = request.POST.get('address')
        phone               = request.POST.get('phone')
        customer            = request.session.get('customer')
        cart                = request.session.get('cart')
        
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer), product=product, price=product.price, address=address, phone=phone,
                          quantity=cart.get(str(product.id)))

            order.save()
        request.session['cart'] = {}

        return redirect('cart')
