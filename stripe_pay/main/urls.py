from django.urls import path
from .views import index
from .views import CreateCheckoutSessionView, SuccessView, CancelView, OrderLandingPageView


urlpatterns = [
    path('', OrderLandingPageView.as_view(), name='landing'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]


