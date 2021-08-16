from django.db import models


class StoryID(models.Model):
    list_id = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-list_id',)

    def __str__(self):
        return self.list_id


class Story(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    descendants = models.IntegerField()
    kids = models.JSONField()
    score = models.IntegerField()
    link = models.TextField()
    time_created = models.DateTimeField()
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    story_id = models.IntegerField(unique=True)
    writer = models.ForeignKey('auth.User', blank=True, null=True, related_name='stories',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', 'time_created', 'type', 'title')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=200)
    kids = models.JSONField()
    story_id = models.ForeignKey(Story, related_name='comments', to_field='story_id', on_delete=models.CASCADE)
    comment_id = models.IntegerField(unique=True)
    comment = models.TextField()
    comment_time = models.DateTimeField()
    type = models.CharField(max_length=50)

    class Meta:
        ordering = ('name', 'comment_time',)

    def __str__(self):
        return self.name


class StoryCounter(models.Model):
    start = models.IntegerField()

    class Meta:
        ordering = ('-start',)



