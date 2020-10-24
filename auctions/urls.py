from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.new_listing, name="create"),
    path("categories", views.categories, name="categories"),
    path("category/<str:categ>", views.category, name="category")
]
