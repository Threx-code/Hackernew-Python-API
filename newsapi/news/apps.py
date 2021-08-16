from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        # please make sure you have run the following command before uncommenting the below code
        # 1. python manage.py makemigrations news
        # 2. python manage.py migrate

        from news import scheduler
        scheduler.run_fetch_top_stories_id()
        scheduler.run_fetch_hn_stories()


