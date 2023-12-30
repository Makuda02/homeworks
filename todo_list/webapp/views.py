from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from .models import Task
from .forms import TaskForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        print(tasks)
        return render(request, 'index.html', {'tasks': tasks})

class TaskView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context

class TaskCreateView(View):
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
            return render(request, "create.html", {"form": form})

class TaskUpdateView(TemplateView):
    template_name = 'create.html'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(instance=task)  # Use 'instance' to pre-fill the form with existing data
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # This will update the existing Task instance
            return redirect('task_update_view', pk=task.pk)
        else:
            return render(request, 'create.html', {'form': form})

class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'create.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')
