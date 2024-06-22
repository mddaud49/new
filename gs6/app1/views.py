from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    institue="cybrom"
    course="python"
    fees=45200
    lis={
        'inst':institue,
        'cu':course,
        'fs':fees,
    }
    return render(request, 'about.html', context=lis,)

def Contact(request):
    name="daud"
    contact=7089678860
    email="dk@gmail.com"
    lis_c={
        'nm':name,
        'con':contact,
        'em':email,
    }
    return render(request, 'contact.html',context=lis_c)