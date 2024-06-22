from django.urls import path
from . import views

urlpatterns=[
    path('about/',views.About,name='about'),
    path('contact/',views.Contact, name='contact')
]