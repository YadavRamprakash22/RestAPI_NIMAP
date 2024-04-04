from django.urls import path,include
from . import views as v
from . import views
from rest_framework import routers


urlpatterns=[
    path("user/",views.UserListCreateAPIView.as_view()),
    path("user/<int:pk>",views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path("client/",views.ClientListCreateAPIView.as_view()),
    path("client/<int:pk>",views.ClientRetrieveUpdateDestroyAPIView.as_view()),
    path("project/",views.ProjectListCreateAPIView.as_view()),
    path("project/<int:pk>",views.ProjectRetrieveUpdateDestroyAPIView.as_view()),
]