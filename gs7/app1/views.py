from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    instname="cybrom"
    place="bhopal"
    company="it"
    dis={
        'nm':instname,
        'pl':place,
        'cm':company,
    }
    return render(request, 'about.html', context=dis ,)


def Contact(request):
    number=7089678860
    place="bhopal"
    institue="cybrom"
    dis_lis={
        'num':number,
        'pl':place,
        'ins':institue,
    }
    return render (request, 'contact.html', context=dis_lis, )

