from django.shortcuts import render, HttpResponseRedirect 
from .forms import ContactForm, SubscriberForm, OrderForm, OrderForm2
from .models import Product, Order
from django.core.paginator import Paginator
from django.views.generic import DetailView


#---FUNCTIONAL VIEWS---#
def indexView(request):
    """
    A functional view for the home page (index.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    MenAccessories =  Product.objects.filter(Category="Men").order_by("-Date_Pub")
    paginator1 = Paginator(MenAccessories, 3)

    WomenAccessories =  Product.objects.filter(Category="Women").order_by("-Date_Pub")
    paginator2 = Paginator(WomenAccessories, 3)

    KidAccessories =  Product.objects.filter(Category="Kids").order_by("-Date_Pub")
    print(KidAccessories)
    paginator3 = Paginator(KidAccessories, 3)

    #---FOR PRODUCT PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj1 = paginator1.get_page(paginator_page_number)

    paginator_page_number = request.GET.get("page")
    page_obj2 = paginator2.get_page(paginator_page_number)

    paginator_page_number = request.GET.get("page")
    page_obj3 = paginator3.get_page(paginator_page_number)
  

    return render(request, "index.html", { 'subscriberForm': subscriberForm , 'MenAccessories':page_obj1, 'WomenAccessories':page_obj2, 'KidAccessories':page_obj3 })


def productView(request):
    """
    A functional view for the product page (product.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    Products =  Product.objects.all().order_by("-Date_Pub")
    paginator = Paginator(Products, 9)

    #---FOR PRODUCT PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)
  
    return render(request, "products.html", { 'subscriberForm': subscriberForm , 'products':page_obj })


def menProductView(request):
    """
    A functional view for the men product page (product.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    Products =  Product.objects.filter(Category="Men").order_by("-Date_Pub")
    paginator = Paginator(Products, 9)

    #---FOR MEN PRODUCT PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)
  
    return render(request, "menProducts.html", { 'subscriberForm': subscriberForm , 'products':page_obj })


def womenProductView(request):
    """
    A functional view for the women product page (product.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    Products =  Product.objects.filter(Category="Women").order_by("-Date_Pub")
    paginator = Paginator(Products, 9)

    #---FOR WOMEN PRODUCT PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)
  
    return render(request, "womenProducts.html", { 'subscriberForm': subscriberForm , 'products':page_obj })


def kidProductView(request):
    """
    A functional view for the kid's product page (product.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    Products =  Product.objects.filter(Category="Kids").order_by("-Date_Pub")
    paginator = Paginator(Products, 9)

    #---FOR KID PRODUCT PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)
  
    return render(request, "kidsProduct.html", { 'subscriberForm': subscriberForm , 'products':page_obj })


def singleProductView(request, uniqueID):
    """
    A functional view for the product page (product.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
    product =  Product.objects.get(uniqueID=uniqueID)
    
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    orderForm = OrderForm(request.POST)
    if request.method == 'POST':
        
        if orderForm.is_valid():
            stock = orderForm.cleaned_data['NoOfStock']

            NewOrder = Order(
                Products=product.Name,
                Price=(int(product.Price) * int(stock)),
                NoOfStock=stock
                )
            get_id = NewOrder.uniqueID
            NewOrder.save()
            product.Stock_Number = str(int(product.Stock_Number) - int(stock))
            product.save()
            product.Stock_Number = str(int(product.Stock_Number) - int(stock))
            product.save()
            return HttpResponseRedirect(f"https://boutique-63is.onrender.com/order/{get_id}")

    return render(request, "singleProduct.html", {'orderForm':orderForm, 'subscriberForm': subscriberForm , 'product':product })

def order(request, id):
    """
    A functional based view for the order competion
    """

    product = Order.objects.get(uniqueID=id)

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    #DATABASE QUERY
    OrderAppend = Order.objects.get(uniqueID=id)
    orderForm2 = OrderForm2(request.POST)

    if orderForm2.is_valid():
            ADDRESS = orderForm2.cleaned_data['Delivery_Address']
            COUNTRY = orderForm2.cleaned_data['Country']
            STATE = orderForm2.cleaned_data['state']
            LGA = orderForm2.cleaned_data['LGA']
            CODE = orderForm2.cleaned_data['Zip_Code']
            MobileNo = orderForm2.cleaned_data['MobileNo']
            Mail = orderForm2.cleaned_data['ClientEmail']

             #APPENDING DATA
            OrderAppend.ClientEmail = Mail
            OrderAppend.MobileNo = MobileNo
            OrderAppend.Delivery_Adress = ADDRESS
            OrderAppend.Country = COUNTRY
            OrderAppend.state = STATE
            OrderAppend.LGA = LGA
            OrderAppend.Zip_Code = CODE

            return render(request, "alert.html", {'orderForm2':orderForm2, 'subscriberForm': subscriberForm , 'product':product })

    return render(request, "orderpage.html", {'orderForm2':orderForm2, 'subscriberForm': subscriberForm , 'product':product })

def aboutView(request):
    """
    A functional based view for the about page (about.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'subscriberForm': subscriberForm })

    return render(request, "about.html", { 'subscriberForm': subscriberForm })


def contactView(request):
    """
    A functional based view for the contact page (contact.html)
    """

    form = ContactForm(request.POST)
    subscriberForm = SubscriberForm(request.POST)

    if request.method == 'POST':
        print(form)
        if form.is_valid():
            form.save()

            return render(request, "alert.html",  { 'subscriberForm': subscriberForm })

    # ---FOR EMAIL SUBSCRIBING---#   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            return render(request, "SusbscribersAlert.html", {'ContactForm':form, 'subscriberForm': subscriberForm })

    return render(request, "contact.html", {'ContactForm':form, 'subscriberForm': subscriberForm })



def alertView(request):
    """
    A functional based view for the alert page (alert.html)
    """

     # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
    return render(request,  "alert.html", {'subscriberForm': subscriberForm })


class RoomImageDisplay(DetailView):

    model = Product
    template_name = 'products.html'
    context_object_name = 'product'