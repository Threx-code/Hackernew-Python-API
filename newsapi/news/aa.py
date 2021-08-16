from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from news.permission import IsWriterOrReadOnly
from news.models import Story, Comment, Writer, StoryID
from news.serializer import StoryIDSerializer, CommentSerializer, StoryListSerializer, \
    StorySerializer
import requests


# class HNList:
#     try:
#         url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
#         payload = {}
#         headers = {}
#         response = requests.request("GET", url, headers=headers, data=payload)
#         # convert the returned data to json serializable data
#         stories_id = response.json()
#
#         # Loop through the Story IDs returned from HN API and store them into the database
#         for i in stories_id:
#             # We don't want to store duplicate Story IDs, so we try and return an
#             # error should the ID be already stored inside the database
#             # This give us ability to store only unique values into the database
#             try:
#                 allID = StoryID(list_id=i)
#                 allID.save()
#             except Exception as e:
#                 print(e)
#
#     except Exception as e:
#         print(e)


# class HNStory:
#     # select the number of storyIDs you want to fetch
#     storyIds = StoryID.objects.all()[:10]
#     # declare an empty list which is going to hold the data from the HN API
#     newData = []
#     # Declare an empty list that will hold the comment from the HN API
#     comments = []
#
#     # loop through the StoryID stored inside the StoryID table and
#     # pass each as a parameter to the HN item API
#     for li in storyIds:
#         url = f"https://hacker-news.firebaseio.com/v0/item/{li}.json?print=pretty"
#         payload = {}
#         headers = {}
#         response = requests.request("GET", url, headers=headers, data=payload)
#         # convert the returned data to json serializable data
#         # append the return serialized data to the list newData variable declared
#         newData.append(response.json())
#
#     # Loop through the newData list.
#     # Store the stories into the Story Table in the database
#     # check if the key['kids'] is not empty
#     #
#     for key in newData:
#         # store stories into the database
#         # We want to be sure each key is not empty, else we passed a default valued
#         try:
#             stories = Story(
#                 name=key['by'] if 'by' in key else '',
#                 descendants=key['descendants'] if 'descendants' in key else 0,
#                 kids=key['kids'] if 'kids' in key else [],
#                 score=key['score'] if 'score' in key else 0,
#                 link=key['url'] if 'url' in key else '',
#                 time_created=key['time'] if 'time' in key else 0,
#                 title=key['title'] if 'title' in key else '',
#                 type=key['type'] if 'type' in key else '',
#                 story_id=key['id'] if 'id' in key else 0,
#                 source='hn',
#             )
#             stories.save()
#
#             # get all the comments for a story
#             # check the length of the comment list, it must be greater than 0
#             if len(key['kids']) > 0:
#                 # Loop through the Story key['kids'] which holds all the comment IDs
#                 # Pass each key['kids'] ID to the url to fetch comments associated to a Story
#                 for mi in key['kids']:
#                     url = f"https://hacker-news.firebaseio.com/v0/item/{mi}.json?print=pretty"
#                     headers = {}
#                     payload = {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     # convert the returned data to json serializable data
#                     # append the return serialized data to the list comments variable declared
#                     comments.append(response.json())
#
#                 # Loop through the return comments response from the HN item API
#                 # store comments to comment table in the Database
#                 # We want to be sure each key is not empty, else we passed a default value
#                 for cm in comments:
#                     try:
#                         story_comments = Comment(
#                             name=cm['by'] if 'by' in cm else '',
#                             kids=cm['kids'] if 'kids' in cm else [],
#                             story_id=Story.objects.get(story_id=stories.story_id),
#                             comment_id=cm['id'] if 'id' in cm else 0,
#                             comment=cm['text'] if 'text' in cm else '',
#                             comment_time=cm['time'] if 'time' in cm else 0,
#                             type=cm['type'] if 'type' in cm else '',
#                         )
#                         story_comments.save()
#                     except Exception as e:
#                         print(e)
#         except Exception as e:
#             print(e)


class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer
    name = 'story-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsWriterOrReadOnly)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    name = 'story-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsWriterOrReadOnly)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


# class NewsList(generics.GenericAPIView):
#     name = 'new-list'
#     HNStory
#
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'news': ('',),
#             'stories': (Story.all(),),
#         })
