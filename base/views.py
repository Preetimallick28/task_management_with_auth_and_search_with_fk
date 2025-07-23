from django.shortcuts import render , redirect
from base.models import add , HistoryModel
from django.db.models import Q

#yellow_underline - currently vscode , this project is using system python software, from system python software we are using for download venv module
# this underline means changing python interpreter - this point should kept in mind
# Create your views here.

#when get() throws error when condition is not matching , the error name is - query does not exist

#__icontains - it is similar like sql like operator
def home(request):
    data=add.objects.filter(host=request.user)
    if request.method=='GET':
        if 'q' in request.GET:
            q_data = request.GET['q']
            print(q_data)
            data = add.objects.filter(Q(title__icontains=q_data) & Q(host=request.user) |Q(desc__icontains=q_data) & Q(host=request.user))
        else:
            data=add.objects.filter(host=request.user)
    return render(request,'home.html',{'data':data})

def add_task(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)
        add.objects.create(
            title = title_data,
            desc = desc_data,
            host = request.user
        )
        return redirect('home')
    return render(request,'add.html')

def update_task(request,pk):
    data = add.objects.get(id=pk)
    if request.method == 'POST':
        title_Data = request.POST['title']
        desc_Data = request.POST['desc']

        # override
        # student.sname - old data
        # name_Data - new data
        data.title = title_Data  
        data.desc = desc_Data
        data.save()
        return redirect('home')

    return render(request,'update.html',{'data':data})


def about(request):
    return render(request,'about.html')

def confirm_delete(request,pk):
    student = add.objects.get(id=pk)
    

    return render(request,'confirm_delete.html',{'task':student})

def delete_(request,pk):
    task=add.objects.get(id=pk)
    HistoryModel.objects.create(title=task.title , desc = task.desc , host = request.user)
    task.delete()
    return redirect('home')

def history(request):
    return render(request,'history.html')
