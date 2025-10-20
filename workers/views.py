from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Worker


class WorkerListView1(ListView):
    model = Worker
    template_name = "workers/workers_list.html"


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker


class WorkerListView2(ListView):
    model = Worker
    template_name = "workers/workers_list2.html"
