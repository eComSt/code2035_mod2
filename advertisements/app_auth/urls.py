from django.urls import path
from .views import login_view,profile_view,logout_view
urlpatterns = [
    path('login/',login_view,name = "login"),
    path('profile/',profile_view,name = "profile"),
    path('logout/',logout_view,name = "logout"),
]
