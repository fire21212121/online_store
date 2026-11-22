from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name = 'catalog')

]