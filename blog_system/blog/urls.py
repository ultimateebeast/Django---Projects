# blog/urls.py
from django.urls import path
from .views import PostList, PostDetail, CategoryView, TagView, create_post

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag_posts'),
    path('create/', create_post, name='create_post'), # New path
]