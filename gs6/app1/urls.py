from django.urls import path
from . import views

urlpatterns = [
    # path('',views.Home ,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact')
]