from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TaskForm
from list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.all().select_related("tag")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy(
            "list:task-detail",
            kwargs={"pk": self.object.pk}
        )


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:index")
