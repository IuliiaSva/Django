from django.urls import path, include
from workers import views
from .views import WorkerListView1, WorkerDetailView, WorkerListView2

app_name = 'workers'
urlpatterns = [
    path('', WorkerListView1.as_view(), name='worker_main'),
    path('worker/<int:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('worker/', WorkerListView2.as_view(), name='worker_update'),
]