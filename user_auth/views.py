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

def profile(request):
    return render(request,'profile.html')

def update_profile(request):
    user_record = User.objects.get(username=request.user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        user_name = request.POST['username']

        user_record.first_name = first_name
        user_record.last_name = last_name
        user_record.email = email
        user_record.username =user_name

        user_record.save()
        return redirect('profile')
    return render(request,'update_profile.html',{'user_record':user_record})

def change_pass(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user)
        old_password=request.POST.get('old_pass')
        u = authenticate(username=request.user , password = old_password)
        if u is not None:
            return render(request,'change_pass.html',{'new_pass':True})
        else:
            return render(request,'change_pass.html',{'wrong_old_pass':True})
    if request.method=='POST':
        new_password = request.POST['new_pass']
        user_record = User.objects.get(username=request.user)
        user_record.set_password(new_password)
        user_record.save()
        return redirect('login')        
    return render(request,'change_pass.html')