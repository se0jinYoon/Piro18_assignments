from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name= 'post_new'),
    path('<int:pk>/post_delete', views.post_delete, name= 'post_delete'),
    path('like_ajax/', views.like_ajax, name= 'like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('comment_del_ajax/', views.comment_del_ajax, name='comment_del_ajax'),
    ]