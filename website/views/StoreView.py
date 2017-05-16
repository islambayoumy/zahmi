from django.shortcuts import render, HttpResponseRedirect, redirect


def home(request):
    return render(request, 'website/store-home.html')\

def product_show(request):
    return render(request, 'website/store-product.html')

