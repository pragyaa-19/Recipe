from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
# login for mantaining the session

def index (request):
    return render(request, 'index.html')

def receipis(request):

    if request.method == "POST":

        data = request.POST
        Receipe_image = request.FILES.get('Receipe_image')
        Receipe_name = data.get('Receipe_name')
        Receipe_dics = data.get('Receipe_dics')
        
        Receipe.objects.create(
        Receipe_name = Receipe_name,
        Receipe_dics = Receipe_dics,
        Receipe_image = Receipe_image,
        )
        return redirect('/receipis')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(Receipe_name__icontains = request.GET.get('search'))



    context = {'receipis': queryset}

    return render(request, 'Receipe_list.html',context) 


def delete_receipis(request,id):
    #handling dynamic urls
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipis')


def update_receipis(request,id):
    #handling dynamic urls
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST


        Receipe_image = request.FILES.get('Receipe_image')
        Receipe_name = data.get('Receipe_name')
        Receipe_dics = data.get('Receipe_dics')

        queryset.Receipe_name = Receipe_name
        queryset.Receipe_dics = Receipe_dics

        if Receipe_image:
            queryset.Receipe_image = Receipe_image


        queryset.save()
        return redirect('/receipis')

   
    context = {'receipis': queryset}
    return render(request, 'update_receipis.html',context) 


def loginpage(request):


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request," invalid username!")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request," invalid password!")
            return redirect('/login/')
    
        else:
            login(request,user)
            return redirect('/receipis/')
        
    return render(request,'login.html')
    
    
def logout(request):
    logout(request)
    return render (request,'')


def register(request):
     

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request," user name exist! please enter anther username")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
    )

        #encrypt password
        user.set_password(password)
        user.save()
        messages.error(request,"Account created sccessfully")

        return redirect('/register/')
    
    return render(request, 'register.html')