from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'ghfufji8vff'})


def eggs(request):
    return HttpResponse("You are a smelly <h1>egg</h1>.")
