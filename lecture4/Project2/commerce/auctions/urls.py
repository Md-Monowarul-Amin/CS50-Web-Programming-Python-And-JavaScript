from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_aucction", views.create_auction, name="create_auction")
]
