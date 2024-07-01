from django.urls import path
from .views import ModulesView


urlpatterns = [
    path("api/v1/", ModulesView.as_view(), name="api/v1"),
]
