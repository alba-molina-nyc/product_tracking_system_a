from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('add_job', AddJobView.as_view(), name='add-job'),

]