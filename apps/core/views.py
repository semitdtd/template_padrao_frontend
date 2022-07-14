from django.shortcuts import render


def index(request):
    bem_vimdo = 'seja bem vindo'
    
    return render(request, 'core/index.html', {'bem_vimdo': bem_vimdo})
