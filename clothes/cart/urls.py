from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('add/<int:id>/', views.add, name='add'),
    path('remove/<int:id>/', views.remove, name='remove'),
    path('pay/', views.pay, name='pay'),
    path('create_order/', views.create_order, name='create_order'),
    path('clear/', views.clear, name='clear'),
    path('', views.cart_detail, name='cart_detail')
]