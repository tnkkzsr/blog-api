from django.contrib import admin
from django.urls import path,include

from rest_framework.views import APIView
from rest_framework.response import Response
from . import views


urlpatterns = [
   #講座続き
   path("posts/",views.PostListCreateView.as_view()),
   path("post/<uuid:pk>/",views.PostRetrieveUpdateDestroyView.as_view()),   
]