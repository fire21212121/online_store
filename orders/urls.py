from django.urls import path
from .views import cart, delivery

urlpatterns = [
path('cart', cart, name='cart'),
path('delivery', delivery, name='delivery'),
]