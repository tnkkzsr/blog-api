from django.contrib import admin
from django.urls import path,include

from rest_framework.views import APIView
from rest_framework.response import Response
from . import views


urlpatterns = [
    
   path("posts/",views.PostCreateView.as_view()),
   path("posts-list/",views.PostListCreateView.as_view()),
   path("posts/<uuid:pk>/", views.PostRetrieveUpdateDestroyView().as_view()),

   
]