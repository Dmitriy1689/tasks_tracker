from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from tasks.models import Habit, Task


class TaskListView(LoginRequiredMixin, ListView):
    """Представление для отображения задач."""

    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 8

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания задачи."""

    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для редактирования задачи."""

    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления задачи."""

    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
