from django.shortcuts import render,redirect
from . models import T
# Create your views here.
def home(request):
    a=T.objects.all().order_by('date_added')

    return render(request,'index.html',{'m':a})


def addTodo(request):
    content=request.POST['content']
    new_item=T(content=content)
    new_item.save()
    return redirect('/')

def deleteTodo(request, todo_id):
    item_to_del=T(id=todo_id)
    item_to_del.delete()
    return redirect('/')