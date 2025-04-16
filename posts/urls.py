from django.urls import path 
from .views import *
from . import views
urlpatterns = [
    path('', BlogPostListView.as_view(), name = 'index'),
    path('homepage', BlogPostListView.as_view(), name = 'homepage'),
    path('post/<str:pk>', BlogPostDetailView.as_view(), name = 'post'),
    path('add', AddPostView.as_view(), name = 'add'),
    path('delete/<str:pk>', views.deletePost, name = 'delete'),
    path('edit/<str:pk>', views.editPost, name = 'edit'),
    # path('login', views.login, name = 'login'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),

]
