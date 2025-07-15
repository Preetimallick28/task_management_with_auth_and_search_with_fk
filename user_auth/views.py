from django.shortcuts import render , redirect
from django.contrib.auth.models import User


# Create your views here.
def login_(request):
    return render(request,'login.html')

def register_(request):
    if request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        user_name = request.POST['username']
        password = request.POST['password']
        print(first_name,last_name,email,user_name,password)
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

