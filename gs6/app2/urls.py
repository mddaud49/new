from django.urls import path
from . import views

urlpatterns=[
    path('shop/',views.Shop, name='shop'),
    path('login/',views.Login, name='login'),
]