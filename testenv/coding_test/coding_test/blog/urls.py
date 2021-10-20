from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, PostDetailView

urlpatterns = [
    # path('home.html',HomePageView.as_view(),name='home'),
    path('',HomePageView.as_view(),name='home'),
    path('contact/',views.ContactPageView,name='contact'),
    path('about/',views.AboutPageView,name='about'),
    path('<str:slug>/',PostDetailView.as_view(),name='post_detail'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
