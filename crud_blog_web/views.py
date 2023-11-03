from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def szablon(request):
    context = {'lista': [1, 2, 3, 4, 5]}
    from crud_blog.models import Hotel
    hotele = Hotel.objects.all()
    context = {'lista':hotele}
    return HttpResponse(loader.get_template('szablon.html').render(context=context))

def apitest(request):
   return JsonResponse({"sampleText": "qwerty"})