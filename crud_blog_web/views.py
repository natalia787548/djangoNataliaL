from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def szablon(request):
    context = {'lista': [1, 2, 3, 4, 5]}




    return HttpResponse(loader.get_template('szablon.html').render(context=context))