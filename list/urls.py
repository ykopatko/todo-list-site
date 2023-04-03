from django.urls import path

from list.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, task_completion
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags", TagListView.as_view(), name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path("/create/", TaskCreateView.as_view(), name="task-create"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task_completion/<int:task_id>/", task_completion, name="task_completion"),
]

app_name = "list"
