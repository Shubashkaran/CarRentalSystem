from django.urls import path
from . import views
urlpatterns=[
    path('register',views.Register,name="Register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('silver',views.silver,name="silver"),
]