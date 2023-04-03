from django.urls import path

from list.views import index

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tag-list"),
]

app_name = "list"
