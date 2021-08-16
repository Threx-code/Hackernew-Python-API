from rest_framework import serializers
from news.models import Story, Comment, StoryID
from django.contrib.auth.models import User


# serializing the comments to allow view display
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'pk', 'name', 'kids', 'story_id', 'comment_id', 'comment', 'comment_time',)


class UserStorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = fields = ('url', 'pk', 'name', 'descendants', 'kids', 'score', 'link',
                           'time_created', 'title', 'type', 'story_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    stories = UserStorySerializer(many=True, read_only=True)


class StorySerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Story
        fields = ('url', 'pk', 'name', 'descendants', 'kids', 'score', 'link',
                  'time_created', 'title', 'type', 'story_id', 'writer', 'comments')


# we want to list only the stories on the landing page
class StoryListSerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Story
        fields = ('url', 'pk', 'name', 'descendants', 'kids', 'score', 'link',
                  'time_created', 'title', 'type', 'story_id', 'writer')


class StoryIDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoryID
        fields = ('url', 'pk', 'list_id',)
