from django.db import models
from datetime import datetime
from uuid import uuid4

# Create your models here.
class Message(models.Model):
    """
    A class based model for storing messages submitted from the contact page
    (contact.html)
    """

    Name = models.CharField(max_length=200, default="Anonymous")
    Email = models.CharField(max_length=50, null=False, blank=False)
    Subject = models.CharField(max_length=500, null=False, blank=False)
    Message = models.TextField(blank=False, null=False)

    def __str__(self):
        """
        A string representation of the Message class
        """

        return self.Name
    

class Subscriber(models.Model):
    """
    A class based model for storing subscribers email adresses
    """

    Name = models.CharField(max_length=200, default="Anonymous")
    Email = models.CharField(max_length=300)


    def __str__(self):
        """
        A string representation of the Subscriber model
        """

        return self.Name
    

class Product(models.Model):
    """
    A class based model for storing products and accessories in the database
    """

    choice = {('Men','Men'), ('Women','Women'), ('Kids', 'Kids')}

    uniqueID = models.UUIDField( default=uuid4, editable=False)
    Name = models.CharField(max_length=200, default="Anonymous")
    Category = models.CharField(max_length=50, blank=True, null=True, choices=choice)
    Price = models.CharField(max_length=50, null=False)
    Stock_Number = models.IntegerField(null=False)
    Date_Pub = models.DateTimeField(default=datetime.now(), editable=False)
    Image = models.ImageField(upload_to="upload") 

    def __str__(self):
        """
        A string representation for the product class based model
        """
        return self.Name



class Order(models.Model):
    """
    A class based model for capturing orders from customers and storing in the database
    """

    choice = {('Pay on delivery','Pay on delivery'), ('Instant payment','Inatant payment'),}

    
    uniqueID = models.UUIDField( default=uuid4, blank=True)
    Products = models.CharField(max_length=200, default="Anonymous", blank=True)
    ClientEmail =  models.CharField(max_length=200, default="Anonymous@gmail.com", blank=True)
    MobileNo =  models.CharField(max_length=200, default="", blank=True)
    PaymentOption = models.CharField(max_length=50, blank=True, null=True, choices=choice)
    Price = models.CharField(max_length=50, null=False, blank=True)
    NoOfStock = models.CharField(max_length=50, null=True, blank=True)
    Date_Pub = models.DateTimeField(default=datetime.now(), editable=False, blank=True)

    def __str__(self):
        """
        A string representation for the order class based model
        """
        return self.Products


class Room(models.Model):
    """
    A class based model for keeping room records
    """

    Title = models.CharField(max_length=200)
    Price = models.CharField(max_length=30)
    Description = models.TextField()
    Star = models.IntegerField()
    Image = models.ImageField(upload_to="upload")
    DatePub = models.DateTimeField(default=datetime.now(), editable=False)


    def __str__(self):
        """
        A string representation of the Room class based model
        """

        return self.Title