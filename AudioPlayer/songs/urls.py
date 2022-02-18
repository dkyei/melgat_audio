from . import views

# Create your tests here.
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]