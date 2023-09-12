from django.contrib import admin
from .models import Message, Product, Subscriber, Room, Order

# Register your models here.
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Subscriber)