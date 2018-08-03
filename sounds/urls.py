from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
    path('post/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('resources', views.resources, name='resources'),
    path('resources/<int:pk>', views.PostListView.as_view(), name='r-detail')

]