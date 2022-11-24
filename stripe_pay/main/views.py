from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import Order
from django.views.generic import TemplateView
from stripe_pay.settings import STRIPE_PUBLIC_KEY


def index(request):
    return render(request, 'main/index.html')


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs["pk"]
        order = Order.objects.get(id=order_id)
        test_domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': order.currency,
                        'unit_amount': int(order.order_price),
                        'product_data': {'name': 'product.name'},
                    },
                    'quantity': 1,
                },
            ],
            metadata={"product_id": order.id},
            mode='payment',
            success_url=test_domain + '/success/',
            cancel_url=test_domain + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})


class SuccessView(TemplateView):
    template_name = "main/success.html"


class CancelView(TemplateView):
    template_name = "main/cancel.html"


class OrderLandingPageView(TemplateView):
    template_name = "main/landing.html"

    def get_context_data(self, **kwargs):
        order = Order.objects.get(id=1)
        context = super(OrderLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "order": order,
            "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY
        })
        return context