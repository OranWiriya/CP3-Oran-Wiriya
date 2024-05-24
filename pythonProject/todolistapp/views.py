from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolistapp.models import Todo

from .forms import CreateUserForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('todolist')
    if( request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('todolist')
        else: 
            messages.info(request, 'Username OR password is incorrect')
            pass
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('todolist')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')

    context ={"form" : form}
    return render(request, 'register.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='index')
def todolist(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        print(title, description)
        todo = Todo.objects.create(
            title = title,
            description = description,
            userCreated = request.user
        )
        todo.save()
        messages.success(request, 'Todo created successfully')
        return redirect('todolist')
    all_todos = Todo.objects.filter(userCreated = request.user) 
    context ={"allTodos" : all_todos}
    return render(request, 'todolist.html', context=context)

@login_required(login_url='index')
def edit(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        messages.success(request, 'Todo updated successfully')
        return redirect('todolist')
    
    todo = Todo.objects.get(id=todo_id)
    context={"todo": todo}
    return render(request, 'edit.html',context=context)

@login_required(login_url='index')
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('todolist')