from django.shortcuts import render,redirect
from base.models import todoModel
from base.models import historyModel
from base.models import restoreModel


# Create your views here.

def home(request):
    all_data=todoModel.objects.all()
    return render(request , 'home.html',{'data': all_data})

def about(request):
    return render(request ,'about.html')


def details(request,pk):
    todo=todoModel.objects.filter(id=pk)
    return render(request , 'details.html',{'data':todo})


def add(request):
    if request.method == 'POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        print(title_data,desc_data)
        todoModel.objects.create(title=title_data,desc=desc_data)
        return redirect('home')
    return render (request, 'add.html')

def edit(request,pk):
    todo=todoModel.objects.get(id=pk)
    if request.method == 'POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        todo.title=title_data
        todo.desc=desc_data
        todo.save()
        return redirect('home')
    return render(request ,'edit.html' , {'data' : todo})

def delete(request,pk):
    todo=todoModel.objects.get(id=pk)

    historyModel.objects.create(title=todo.title,desc=todo.desc)
    todo.delete()
    return redirect('home')



def history(request):
    History=historyModel.objects.all()
    return render(request , 'history.html',{'History':History})


def delete_all_history(request):

    history_record=historyModel.objects.all()

    for i in history_record:
        restoreModel.objects.create(title=i.title,desc=i.desc)


    History=historyModel.objects.all()
    History.delete()
    return redirect('history')


def restore_all_history(request):
    restoring_history=restoreModel.objects.all()

    for i in restoring_history:
        historyModel.objects.create(title=i.title,desc=i.desc)

    restoring_history.delete()
    return redirect('history')

def delete_history(request,pk): 
    History=historyModel.objects.get(id=pk)
    History.delete()
    return redirect('history')

