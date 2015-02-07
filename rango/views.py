from django.http.response import HttpResponse

# Create your views here.
from django.shortcuts import render


def index(request):
    message = {"test_message":"Un message de test. "}
    return render(request, 'rango/index.html', message)

def about(request):
    return render(request, 'rango/about.html')