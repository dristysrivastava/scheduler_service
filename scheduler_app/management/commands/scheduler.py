from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from scheduler_app.utils import send_discount_offer, send_morning_report
from scheduler_app.models import ScheduledJob

scheduler = BackgroundScheduler()


def schedule_jobs(check_task_scheduled_flag=False):

    if not check_task_scheduled_flag:
        cron_jobs = ScheduledJob.objects.filter(task_scheduled=True)
        for cron_job in cron_jobs:
            cron_expression = cron_job.cron_expression
            task = cron_job.task

            scheduler.add_job(globals()[task], CronTrigger.from_crontab(cron_expression))
            print(f"{cron_job} scheduled")
    else:
        cron_jobs = ScheduledJob.objects.filter(task_scheduled=False)
        for cron_job in cron_jobs:
            cron_expression = cron_job.cron_expression
            task = cron_job.task

            scheduler.add_job(globals()[task], CronTrigger.from_crontab(cron_expression))
            cron_job.task_scheduled = True
            cron_job.save()
            print(f"{cron_job} scheduled")


class Command(BaseCommand):
    help = "Schedule jobs for sending notifications"

    def handle(self, *args, **options):
        try:
            schedule_jobs()
            scheduler.start()
            while True:
                schedule_jobs(True)
                # scheduler.print_jobs()
        except KeyboardInterrupt:
            scheduler.shutdown()
