from django.urls import path
from .views import AddCategoryView, ArticleDetailView, HomeView, AddPostView, UpdatePostView, DeletePostView, CategoryView, CategoryListView, LikeView
# from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('articles/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]   