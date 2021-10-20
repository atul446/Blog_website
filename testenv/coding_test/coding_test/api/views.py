from django.shortcuts import render
from rest_framework import generics ,permissions
from blog.models import Post
from .serializers  import PostSerializer

# Create your views here.

class PostApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSerializer

class PostApiDetailView(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSerializer
