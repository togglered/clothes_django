from django.conf import settings
from main.models import ProductSize


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, size):
        if str(size.id) in self.cart:
            self.cart[str(size.id)]["quantity"] += 1
        else:
            self.cart[str(size.id)] = {
                'quantity': 1
            }
        self.save()

    
    def remove(self, size):
        if str(size.id) in self.cart and self.cart[str(size.id)]["quantity"] > 0:
            self.cart[str(size.id)]["quantity"] -= 1
        self.save()

    
    def __iter__(self):
        for product in self.cart:
            yield product

    
    def save(self):
        self.session.modified = True

    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]