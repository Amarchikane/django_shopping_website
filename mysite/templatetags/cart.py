from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(Products  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Products.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(Products  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Products.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(Products  , cart):
    return Products.price * cart_quantity(Products , cart)


@register.filter(name='total_cart_price')
def total_cart_price(Products , cart):
    sum = 0 ;
    for p in Products:
        sum += price_total(p , cart)

    return sum