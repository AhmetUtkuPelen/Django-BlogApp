from django.urls import path
from .views import*


urlpatterns = [
    path('login/',login_request,name="login"),
    path('register/',register_request,name="register"),
    path('logout/',logout_request,name="logout"),
]
