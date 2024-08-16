from django.urls import path
from app import views
urlpatterns = [
    path('h1/',views.register),
    # path('home/',views.home),
    path('registerdata/',views.registerdata,name='register')
]