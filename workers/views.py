from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Worker


class WorkerListView1(ListView):
    model = Worker
    template_name = "workers/workers_list.html"
    context_object_name = "workers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker_count'] = Worker.objects.count()
        context['object_list'] = Worker.objects.order_by('-date_of_joining')[:4]
        return context


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker


class WorkerListView2(ListView):

    model = Worker
    template_name = "workers/workers_list2.html"
    paginate_by = 10
