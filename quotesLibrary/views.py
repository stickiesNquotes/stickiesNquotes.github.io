from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

from .models import *


def authors(request):
    template = loader.get_template('quotes.html')
    context = {
        'authors': Author.objects.all()
    }
    return HttpResponse(template.render(context, request))

def quote(request, id):
    template = loader.get_template('indivQuote.html')
    context = {
        'quote': Quote.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def myStickyNote(request):
    template = loader.get_template('myStickyNote.html')
    return HttpResponse(template.render(request))

def snakey(request):
    template = loader.get_template('snakey.html')
    return HttpResponse(template.render(request))

def designDocumentation(request):
    template = loader.get_template('designDocumentation.html')
    return HttpResponse(template.render(request))
