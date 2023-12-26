from django.shortcuts import render
from . import models, forms
from translate import Translator


def index(request):
    if request.method == 'POST':
        lang = request.POST.get('lang', None)
        lang_to = request.POST.get('lang_to', None)
        txt = request.POST.get('txt', None)

        translator = Translator(from_lang=lang, to_lang=lang_to)
        translation = translator.translate(txt)

        return render(request, 'index.html', {'result': translation})

    return render(request, 'index.html')
# Create your views here.
