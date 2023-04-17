from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormacaoForm


def formacao(request):

    form = FormacaoForm

    if request.method == 'POST':
        form = FormacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Ok")

    context = {
        'form': form
    }

    return render(request, 'formacao/profissional.html', context=context)
