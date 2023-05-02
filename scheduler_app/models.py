from django.db import models


class ScheduledJob(models.Model):
    cron_expression = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    task_scheduled = models.BooleanField(default=False)

    def __str__(self):
        return f"Schedule {self.task} for {self.cron_expression} is scheduled and its status is: {self.task_scheduled}"

