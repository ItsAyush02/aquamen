from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index.as_view(), name= "index"),
    path("customer/", views.CustomerRegistration.as_view(), name="customer"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("supplier/", views.Supplier.as_view(), name="supplier"),
    path("locate/", views.List.as_view(), name="locate"),
    path("locate/<int:pk>/", views.DetailListView.as_view(), name="list-detail"),
    path("locate/checkout/", views.Checkout, name="checkout"),

    path("thanks/", views.Thanks.as_view(), name="thanks"),
    path("customer/signup/", views.signup, name="signup"),
    path("customer/sign_in/", views.sign_in, name="sign_in"),
    # path("login/", views.login, name="login"),
    # path("signout/", views.signout, name="signout"),

] 
