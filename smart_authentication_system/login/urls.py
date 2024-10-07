from django.urls import path
from login.views import login
from signup.views import logout
urlpatterns = [
    path('login/',login,name="login"),
    path('logout/',logout,name="logout")
    
]
