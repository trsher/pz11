from django.shortcuts import render, HttpResponse

# Create your views here.

def index (request):
    return HttpResponse("<h1>Hello, world!<h1>")

def second_page (request):
    return render(request, "second_page.html")

def index1 (request):
    return render(request, "1.html")

def index2 (request):
    return render(request, "2.html")

def index3 (request):
    return render(request, "3.html")

def index4 (request):
    return render(request, "4.html")

def index5 (request):
    return render(request, "5.html")
