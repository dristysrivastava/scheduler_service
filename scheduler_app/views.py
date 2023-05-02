from rest_framework import viewsets

from scheduler_app.models import ScheduledJob
from scheduler_app.serializers import ScheduledJobSerializer


class ScheduledJobViewSet(viewsets.ModelViewSet):
    queryset = ScheduledJob.objects.all()
    serializer_class = ScheduledJobSerializer
