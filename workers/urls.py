from django.urls import path

from .views import WorkerDetailView, WorkerListView1, WorkerListView2

app_name = "workers"
urlpatterns = [
    path("", WorkerListView1.as_view(), name="worker_main"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"),
    path("worker/", WorkerListView2.as_view(), name="worker_update"),
]
