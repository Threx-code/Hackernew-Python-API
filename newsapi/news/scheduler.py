from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from news.views import fetch_top_stories_id, fetch_hn_stories


# since the HN Top Stories IDs are only updated few time a day, we would set
# the scheduler to run every six hours
def run_fetch_top_stories_id():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(fetch_top_stories_id, 'interval', hours=6)
    scheduler.start()


# We would run this every 5 minutes to fetch new data
def run_fetch_hn_stories():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(fetch_hn_stories, 'interval', minutes=2)
    scheduler.start()

