from django.shortcuts import render
from django.views import View

from App.models.orders import Order

from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class OrderView(View):

    def get(self , request ):
        customer    = request.session.get('customer')
        orders      = Order.get_orders_by_customer(customer)

        return render(request , 'orders.html'  , {'orders' : orders})

@csrf_exempt
def order_complete(request):
    if request.method == "POST":
        if Order.objects.filter(status=False, customer=request.session['customer']).count() == 0:
            return JsonResponse({'saved':False})
        else:
            Order.objects.filter(status=False, customer=request.session['customer']).update(status=True)
    return render(request, 'order_complete.html')