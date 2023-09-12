from django.forms import ModelForm
from .models import Message, Room, Subscriber, Order
from django import forms

class ContactForm(ModelForm):
    """
    A class based form for capturing data and storing in the database
    """

    class Meta:
        model = Message
        fields = "__all__"



class SubscriberForm(ModelForm):
    """
    A class based form for capturing data and storing in the database
    """

    class Meta:
        model = Subscriber
        fields = "__all__"


class OrderForm(forms.Form):
    """
    A class based form for capturing data and storing in the database
    """

    choice = {('Pay on delivery','Pay on delivery'), ('Instant payment','Inatant payment'),}

    PayOption = forms.CharField(max_length=50)
    NoOfStock = forms.CharField(max_length=50)