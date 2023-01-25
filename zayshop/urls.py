"""zayshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page import views as pages_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages_views.index, name='index'),
    path('', pages_views.index, name='home'),
    path('about/', pages_views.about, name='about'),
    path('shop/', pages_views.shop, name='shop'),
    path('contact/', pages_views.contact, name='contact'),
    path('login/', pages_views.login_request, name='login'),
    path('register/', pages_views.register_request, name='register'),
    path('logout/', pages_views.logout_request, name='logout'),
    path('cart/',pages_views.cart, name='cart'),
    path('payment/',pages_views.payment, name='payment'),
    path('add-product/<int:product_id>',pages_views.add_product, name="add_product"),
    path("cart", pages_views.cart, name="cart"),
    path("delete-cart-product/<int:cart_product_id>", pages_views.delete_cart_product, name="delete_cart_product"),
    path("set-cart-product/<int:cart_product_id>", pages_views.set_cart_product_quantity, name="set_cart_product_quantity")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
