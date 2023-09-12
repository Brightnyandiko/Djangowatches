from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Product(request):
    return render(request, 'product.html')


def Testimonial(request):
    return render(request, 'testimonial.html')
