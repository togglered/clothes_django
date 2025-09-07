from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.product_info, name='product_info'),
    path('<str:category_slug>/<str:subcategory_slug>/', views.subcategory, name='subcategory')
]