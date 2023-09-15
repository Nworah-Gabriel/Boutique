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

    NoOfStock = forms.CharField(max_length=50)

class OrderForm2(forms.Form):
    """
    A class based form for capturing data and storing in the database
    """
    ClientEmail =  forms.CharField(max_length=200)
    MobileNo =  forms.CharField(max_length=200)
    Delivery_Address = forms.CharField(max_length=400)
    Country = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    LGA = forms.CharField(max_length=200)
    Zip_Code = forms.CharField(max_length=200)