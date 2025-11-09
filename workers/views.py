from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from rest_framework import status, viewsets, mixins, permissions
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Worker
from workplaces.models import Workplaces
from .serializers import WorkerSerializer, WorkplacesSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters

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
class WorkerFilter (filters.FilterSet):
    class Meta:
        model = Worker
        fields = {
            'grade': ['gte'],  # >=
            'skills': ['exact'],
        }


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = WorkerFilter
    permission_classes = (AllowAny,)


class WorkplacesViewSet(viewsets.ModelViewSet):
    queryset = Workplaces.objects.all()
    serializer_class = WorkplacesSerializer
