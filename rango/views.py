from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    #return  HttpResponse("<h1>Hello World</h1> <br><br>Click <a href=/rango/about/>here </a> for About page ")
    context_dict = {"boldmessage" : "this is index page"}
    return render(request, "rango/index.html", context_dict)
def about(request):
    return render(request, "rango/about.html", {})
