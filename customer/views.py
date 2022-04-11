from re import template
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Orders, SupplierList

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/ContactUs.html')

class Supplier(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/Under-construction.html')

class List(ListView):
    model = SupplierList
    template_name = "customer/list.html"
    context_object_name = "list_page"

class DetailListView(DetailView):
    model = SupplierList
    template_name = "customer/detail_page.html"
    context_object_name = "list_detail"

def Checkout(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        number = request.POST['number']
        email = request.POST['email']
        quantity = request.POST['quantity']
        address = request.POST['address'] + " " + request.POST['address2']
        state = request.POST['state']
        city = request.POST['city']
        zip = request.POST['zip']

        order = Orders(first_name=first_name, last_name=last_name, email=email, number=number, address=address, city=city, zip=zip, quantity=quantity)

        order.save()
        thank = True
        return render(request, "customer/checkout1.html", {'thank': thank})
    
    return render(request, "customer/checkout1.html")
    


    



class Thanks(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/thanks.html')


class CustomerRegistration(View):
    def get(self, request, *args, **kwargs):
        return render(request, "customer/customer.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['email']
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        number = request.POST.get("number")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('index')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('index')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')


        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.number = number

        my_user.is_active = False

        my_user.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect("customer")


def sign_in(request):
    if request.method == "POST":
        username = request.POST["email"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Successfully!!")
            return render(request, "customer/index.html", {"fname":fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect("index")

    return render(request, "customer/customer.html")












