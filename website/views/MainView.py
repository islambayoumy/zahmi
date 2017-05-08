from django.shortcuts import render, HttpResponseRedirect, redirect


def index(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about_us.html')


