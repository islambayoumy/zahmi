from django.shortcuts import render, HttpResponseRedirect, redirect


def show(request):
    return render(request, 'website/championship.html')


