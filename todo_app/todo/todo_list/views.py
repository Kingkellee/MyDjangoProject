from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_todos = List.objects.all
            messages.success(request, ('Your Todo Has Been added to The List'))
            return render(request, 'home.html', {'all_todos': all_todos})
    else:
        all_todos = List.objects.all
        return render(request, 'home.html', {'all_todos': all_todos})

def delete(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.delete()
    messages.success(request, ('Todo Has Been Removed Successfuly'))
    return redirect('home')


def cross_off(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.completed = True
    todo.save()
    return redirect('home')


def uncross(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.completed = False
    todo.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        todo = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ("Your Todo Has been Changed"))
            return redirect('home')
    else:
        todo = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'todo': todo})



# Create your views here.
