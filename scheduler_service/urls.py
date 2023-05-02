from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from scheduler_app.views import ScheduledJobViewSet

router = routers.DefaultRouter()
router.register('scheduled-jobs', ScheduledJobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
