from django.urls import path
from .views import PostApiDetailView, PostApiView

urlpatterns = [
    path('',PostApiDetailView.as_view(),name='api_detail'),
    path('<int:pk>',PostApiView.as_view(),name='list'),

]
