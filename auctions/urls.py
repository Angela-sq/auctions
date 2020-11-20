from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.new_listing, name="create"),
    path("categories", views.categories, name="categories"),
    path("category/<str:categ>", views.category, name="category"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("viewlisting/<int:product_id>", views.viewlisting, name="viewlisting"),
    path("addcomment/<int:product_id>", views.addcomment, name="addcomment"),
    path("addtowatchlist/<int:product_id>",
         views.addtowatchlist, name="addtowatchlist"),
    path("closebid/<int:product_id>", views.closebid, name="closebid"),
    path("closedlisting", views.closedlisting, name="closedlisting")
]
