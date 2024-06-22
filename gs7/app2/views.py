from django.shortcuts import render

# Create your views here.
def Shop(request):
    return render(request, 'shop.html')
