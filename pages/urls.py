from django.urls import path
from .views import IndexView
from .views import AboutView
from .views import LoginView
from .views import RegisterView
from .views import RecoverPasswordView
from .views import DefaultView


urlpatterns = [
    path("default_html/", DefaultView.as_view(), name="default_html"),
    path("home/", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "recover_password/", RecoverPasswordView.as_view(), name="recover_password"
    ),
]
