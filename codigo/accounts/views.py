from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm


def cadastrar(request):

    form = UserRegisterForm

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/accounts/login")

    context = {
        'form': form
    }

    return render(request, 'registration/cadastrar.html', context=context)
