from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from rest_framework import status, viewsets, mixins
from rest_framework.views import APIView
from .models import Worker
from .serializers import WorkerSerializer
from rest_framework.response import Response

class WorkerListView1(ListView):
    model = Worker
    template_name = "workers/workers_list.html"
    context_object_name = "workers"

    def get_queryset(self):
        return (Worker.objects
                .select_related('workplace')
                .prefetch_related('images')
                .all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker_count'] = Worker.objects.count()
        context['object_list'] = (Worker.objects
                              .select_related('workplace')
                              .prefetch_related('images')
                              .order_by('-date_of_joining')[:4])
        return context

class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker

    def get_queryset(self):
        return (Worker.objects.select_related('workplace')
                .prefetch_related('images').all())


class WorkerListView2(ListView):

    model = Worker
    template_name = "workers/workers_list2.html"
    paginate_by = 10

    def get_queryset(self):
        return (Worker.objects.select_related('workplace')
                .prefetch_related('images').all())

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
