from .models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User

def categories(request):
    # list of products available
    return render(request, "auctions/categories.html")

@login_required(login_url='/login')
def category(request, categ):
    # retieving all the products that fall into this category
    categ_products = Listing.objects.filter(category=categ)
    empty = False
    if len(categ_products) == 0:
        empty = True
    return render(request, "auctions/category.html", {
        "categ": categ,
        "empty": empty,
        "products": categ_products
    })


def new_listing(request):
    if request.method == "POST":
        # item is of type Listing (object)
        item = Listing()
        # assigning the data submitted via form to the object
        item.seller = request.user.username
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.category = request.POST.get('category')
        item.starting_bid = request.POST.get('starting_bid')
        # submitting data of the image link is optional
        if request.POST.get('URL'):
            item.URL = request.POST.get('URL')
        else:
            item.URL = "https://www.aust-biosearch.com.au/wp-content/themes/titan/images/noimage.gif"
        # saving the data into the database
        item.save()
        return render(request, "auctions/index.html")
    # if request is get
    else:
        return render(request, "auctions/new_listing.html")


def index(request):
    # list of products available
    products = Listing.objects.all()
    # checking if there are any products
    empty = False
    if len(products) == 0:
        empty = True
    return render(request, "auctions/index.html", {
        "products": products,
        "empty": empty
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
