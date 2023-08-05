from django.shortcuts import render,redirect
from django . http import HttpResponse
from .models import task
from . forms import todoform
from django . views . generic .list import ListView
from django . views . generic .detail import DetailView
from django . views . generic .edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# list view
class tasklistview(ListView):
    model=task
    template_name='index.html'
    context_object_name='tasks'

# detail view

class taskdetailview(DetailView):
    model=task
    template_name='detail.html'
    context_object_name='tasks'
# update view
class taskupdateview(UpdateView):
    model=task
    template_name='update.html'
    context_object_name='tasks'
    fields=['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
# delete view
class taskdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')
def index(request):
    tasks = task.objects.all()
    if request.method == "POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
        return redirect('/')
    return render (request,'index.html',{'tasks':tasks})
# def details(request):
#     # tasks=task.objects.all()
#     return render(request,'detail.html',{'tasks':tasks})
def delete(request,task_id):
    tasks = task.objects.get(id=task_id)
    if request.method == "POST":
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    tasks=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'tasks':tasks})

