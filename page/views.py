from django.shortcuts import render, redirect
from page.models import Product,Cart,CartProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('product_id')[:3]
    context = {
        'products' : products,
        }    
    return render(request, 'index.html',context)


def about(request):
    
    return render(request, 'about.html')


def contact(request):
    
    return render(request, 'contact.html')

def payment(request):
    
    return render(request, 'payment.html')


def shop(request):
    
    context = dict()
    
    context['products'] = Product.objects.all()
     
    return render(request, 'shop.html', context)


def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username, password = password )
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {
                'error': 'username ya da parola yanlis'
            })
            
    return render(request, 'login.html')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', 
                {
                    "error":"username kullaniliyor",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', 
                    {
                        "error":"email kullaniliyor",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname,
                    last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, 'register.html', 
            {
                "error":"parola eslesmiyor",
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname
            })
    
    return render(request, 'register.html')

def logout_request(request):
    logout(request)
    return redirect('home')


def add_product(request, product_id):
    if request.method == "POST":
        cartCheck = Cart.objects.filter(user_id = request.user.id).count()
        if cartCheck == 0:
            newCart = Cart.objects.create(user_id = request.user.id)
        cart = Cart.objects.filter(user_id = request.user.id).first()
        productCheck = CartProduct.objects.filter(product_id = product_id, cart_id = cart.cart_id).count()

        if productCheck == 0:
            CartProduct.objects.create(product_id = product_id, cart_id = cart.cart_id, quantity=1)
        else:
            cartProduct = CartProduct.objects.filter(product_id = product_id, cart_id = cart.cart_id).first()
            cartProduct.quantity = cartProduct.quantity + 1
            cartProduct.save()
    return redirect('home')

def cart(request):
    cartTotal = 0
    shipping = 100
    cartCheck = Cart.objects.filter(user_id = request.user.id).count()
    if cartCheck == 0:
        newCart = Cart.objects.create(user_id = request.user.id)
    cart = Cart.objects.filter(user_id = request.user.id).first()
    cartproducts = CartProduct.objects.filter(cart_id = cart.cart_id).select_related()
    
    for cartProduct in cartproducts:
        cartTotal += float(cartProduct.product.product_price) * float(cartProduct.quantity)

    context = {
        'cartproducts' : cartproducts,
        'cartTotal' : cartTotal,
        'shipping' : shipping
    }
    return render(request, "cart.html", context)

def delete_cart_product(request, cart_product_id):
    if request.method == "POST":
        CartProduct.objects.filter(id = cart_product_id).delete()
    
    return redirect('cart')

def set_cart_product_quantity(request, cart_product_id):
    if request.method == "POST":
        data = request.POST
        set_type = data.get("setType")
        cartProduct = CartProduct.objects.get(id = cart_product_id)
        if set_type == 'decrease':
            if cartProduct.quantity == 1:
                CartProduct.objects.filter(id = cart_product_id).delete()
            else:
                cartProduct.quantity = cartProduct.quantity - 1
                cartProduct.save()
        else:
            cartProduct.quantity = cartProduct.quantity + 1
            cartProduct.save()
    
    return redirect('cart')

