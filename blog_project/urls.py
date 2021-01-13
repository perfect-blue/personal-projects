from django.urls import path
from . import views

app_name = 'blog_project'
urlpatterns = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('about/',views.AboutView.as_view(), name='about_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]
