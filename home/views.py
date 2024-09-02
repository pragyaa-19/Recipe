# logical part
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name': 'pragya rathore', 'age': 20},
        {'name': 'prisha rathore', 'age': 21},
        {'name': 'priya rathore', 'age': 22},
        {'name': 'preksha rathore', 'age': 13}
    ]

    return render(request , "home/index.html",context={'peoples': peoples} )

def pragya(request):
    return HttpResponse("<b>the server is working for sure </b>")