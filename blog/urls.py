# from .views import PostList
# from django.urls import path

# urlpatterns = [
#     path('', PostList.as_view(), name='home'),
#     # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# ]


from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]