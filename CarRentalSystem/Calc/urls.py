from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('Booking',views.booking,name="Booking"),
    path('camp',views.camp,name="Book"),
    path('Success',views.Success,name="Success"),
    path('redirect1',views.redirect1,name="redirect1"),

]