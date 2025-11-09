from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerDetailView, WorkerListView1, WorkerListView2, WorkerViewSet, WorkplacesViewSet

app_name = "workers"

router = DefaultRouter()
router.register(r"workers", WorkerViewSet)
router.register(r"workerplaces", WorkplacesViewSet)

urlpatterns = [
    path("", WorkerListView1.as_view(), name="worker_main"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"),
    path("worker/", WorkerListView2.as_view(), name="worker_update"),
    path ("", include(router.urls)),
]
