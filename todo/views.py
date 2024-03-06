from django.shortcuts import render
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Task



class TaskCreate(CreateView):
    model = Task
    fields = ['title','description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            # If user is authenticated, assign the task to the authenticated user
            messages.success(self.request, "The task was created successfully.")
            form.instance.user = self.request.user
        else:
            # If user is not authenticated, handle anonymous user or create a default user
            # For example, you can create a default user for anonymous tasks:
            anonymous_user = User.objects.get_or_create(username='anonymous')[0]
            form.instance.user = anonymous_user
            messages.success(self.request, "The task was created successfully.")
        return super(TaskCreate,self).form_valid(form)



class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
   


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate,self).form_valid(form)
    


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)




def home(request):
    return render(request,'home.html')