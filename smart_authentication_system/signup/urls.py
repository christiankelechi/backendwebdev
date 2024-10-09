from django.urls import path
from signup.views import signup,welcome_page
urlpatterns = [
    path('signup/',signup,name="signup"),
    path('welcome_page/',welcome_page,name="welcome_page")
]