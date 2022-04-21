from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import Todoforms
from  . models import task
from django.views.generic import  ListView
from  django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class delete_view(DeleteView):
    model = task
    template_name = 'details.html'
    success_url = reverse_lazy('cbvhome')


class update_view(UpdateView):
    model = task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class detail_view(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = "task"

class list_view(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task'

def add(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority,date=date)
        task1.save()

    return render(request,'home.html',{'task':task2})
#def details(request):

   # return render(request,'details.html',{'task':task1})
def delete(request,taskid):
    if request.method=='POST':
        task1 = task.objects.get(id=taskid)
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task1=task.objects.get(id=id)
    f=Todoforms(request.POST or None,instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task1})
