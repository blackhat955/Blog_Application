from django.shortcuts import render


def home(request):
    return render(request,'nav/nav.html')

def hello(request):
    return HttpResponse('<h1> Hello World </h1>')