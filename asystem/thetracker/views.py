from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Job
from .filters import JobFilter
from django.contrib.auth.mixins import PermissionRequiredMixin
    
class HomeView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    fields = '__all__'

    def get_total_amount(self, **kwargs):
        # total = num_stones * .50 
        pass

class AddJobView(PermissionRequiredMixin, CreateView):
    permission_required = 'jobs.add_jobs'
    model = Job
    template_name = 'add_job.html'
    fields = '__all__'

