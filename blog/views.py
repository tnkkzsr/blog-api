from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

#APIViewで書き換え
class PostCreateView(APIView):

    def post(self,request):
        if not request.user.is_authenticated:
            return Response({"message":"fail"},status=403)
        serializer = PostSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)



#APIViewで書き換え
class PostListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        if not request.user.is_authenticated:
            return Response({"message":"fail"},status=403)
        
        serializer = PostSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    

    
class PostRetrieveUpdateDestroyView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
    
    def get(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    def put(self,request,pk):
        if not request.user.is_authenticated:
            return Response({"message":"fail"},status=403)
        
        post = self.get_object(pk)

        if not post:
            return Response({"message":"fail"},status=404)
        
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)