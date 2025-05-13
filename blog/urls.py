from django.urls import path, include
from . import views

urlpatterns = [
path('postComment', views.postComment, name="postComment"),
path('', views.blogHome, name="bloghome"),
path('<str:slug>', views.blogPost, name="blogPost"),
path('category_blogs/<str:slug>/', views.category_blogs, name='category_blogs'),
path('tag_blogs/<str:slug>/', views.tag_blogs, name='tag_blogs'),
]