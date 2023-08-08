from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated

from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]