from django import template

register = template.Library()

def find_total(value, arg):
    return float(value) * float(arg)

def find_cart_total(value, arg):
    return float(value) + float(arg)

register.filter('find_total', find_total)
register.filter('find_cart_total', find_cart_total)