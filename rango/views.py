from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.

def index(request):
    #return  HttpResponse("<h1>Hello World</h1> <br><br>Click <a href=/rango/about/>here </a> for About page ")
    category_list = Category.objects.order_by("-likes")[:5]
    context_dict = {'categories': category_list}
    return render(request, "rango/index.html", context_dict)

def about(request):
    return render(request, "rango/about.html", {})
