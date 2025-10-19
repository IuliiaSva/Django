from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Worker
from django.http import HttpResponse

class WorkerListView1(ListView):
        model = Worker
        template_name = 'workers/workers_list.html'
class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
class WorkerListView2(ListView):
    model = Worker
    template_name = 'workers/workers_list2.html'
# Create your views here.
