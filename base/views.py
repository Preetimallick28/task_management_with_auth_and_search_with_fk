from django.shortcuts import render , redirect
from base.models import add , HistoryModel , CompleteModel
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
    all_history = HistoryModel.objects.all()
    return render(request,'history.html',{'all_history':all_history})

def delete_history(request,pk):
    data=HistoryModel.objects.filter(id=pk)
    data.delete()
    return redirect('history')


def restore_history(request,pk):
    restore_article = HistoryModel.objects.get(id=pk)
    add.objects.create(title=restore_article.title,desc=restore_article.desc , host=request.user)
    restore_article.delete()
    return redirect('home')

def clear_all(request):
    clear_all = HistoryModel.objects.filter(host=request.user)
    # we didnt use all() method because we dont want delete other users record , we have to delete record of specific user only
    clear_all.delete()
    return redirect('history')

def restore_all(request):
    restore_his_all = HistoryModel.objects.all()
    for i in restore_his_all:
        add.objects.create(title=i.title,desc=i.desc,host=request.user)
    restore_his_all.delete()
    return redirect('home')

def complete_task(request,pk):
   data = add.objects.get(id=pk)
   CompleteModel.objects.create(title=data.title , desc = data.desc , host = request.user)
   data.delete()
   return redirect('completetask_list')

def completetask_list(request):
    complete_task = CompleteModel.objects.all()
    return render(request,'completetask_list.html',{'task':complete_task}) 