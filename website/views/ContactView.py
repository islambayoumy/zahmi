from django.shortcuts import render, HttpResponseRedirect, redirect


def contact(request):
    return render(request, 'website/contact_us.html')


