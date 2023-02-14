from django.shortcuts import redirect, render
from accounts.forms import RegisterUserForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

def RegisterUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts/login')
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }    

    return render(request, 'registration/cadastro.html',context=context)


