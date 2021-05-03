from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# third party import
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSErializer
from rest_framework import generics
from rest_framework import mixins

from .models import Post

class TestView(APIView):
  permission_classes = (IsAuthenticated, )
  def get(self, request, *args, **kwargs):
    querry = Post.objects.all()
    post = querry.first()
          # serializer = PostSErializer(querry, many=True)
    serializer = PostSErializer(post)
    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    serializer = PostSErializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

class PostView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                 generics.GenericAPIView):

   serializer_class = PostSErializer
   queryset = Post.objects.all()

   def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

   def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSErializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSErializer
    queryset = Post.objects.all()