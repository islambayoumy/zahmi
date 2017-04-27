from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth
from website.forms import RegisterationForm

'''
def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('/account')
    else:
        form = RegisterationForm()
        args = {
            'form': form
        }
        return render(request, 'accounts/register.html', args)
'''


#reverse('accounts:logout')