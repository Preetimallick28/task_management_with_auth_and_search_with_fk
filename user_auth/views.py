from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout


# Create your views here.
def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        u=authenticate(username=username , password = password) #to match the credential we use authenticate , authenticate function return entire record
        if u is not None:
            login(request,u) #request is module where all credential will store
            return redirect('home')
        else:
            return render(request,'login.html',{'wrong_credential':True})
    return render(request,'login.html')



def register_(request):
    if request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        user_name = request.POST['username']
        password = request.POST['password']
        print(first_name,last_name,email,user_name,password)
        try:
            username_exist = User.objects.get(username=user_name)
            return render(request,'register.html',{'username_existed':True})
        except:
            u=User.objects.create(
                first_name=first_name,
                last_name = last_name,
                email = email,
                username = user_name
            )
            u.set_password(password)
            u.save()
            return redirect('login')
    return render(request,'register.html')

def logout_(request):
    logout(request) #it will clear the credential from sessison storage
    return redirect('login')

