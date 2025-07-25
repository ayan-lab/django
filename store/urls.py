from django.urls import path
from rest_framework import routers
from . import views
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('carts', views.CartViewSet, basename='cart')
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewset, basename='orders')
router.register('products', views.ProductViewSet, basename='products')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewset, basename='cart-items')


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', views.ProductImageViewset, basename='product-images')



urlpatterns =  [
    path("collections/", views.Collection_list.as_view()),
    path("collections/<int:pk>", views.Collection_detail),
]

urlpatterns = urlpatterns + router.urls + carts_router.urls + products_router.urls