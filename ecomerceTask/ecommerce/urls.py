from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('detail_product/<int:item_id>/',views.detail_product, name='detail_product'),
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
]
