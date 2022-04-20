from django.urls import path, re_path
from .import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, TagIndexView, LikeView, AddCommentView #, UserProfileView #, BootstrapFilterView  #, LocationPostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"), #has a empty strting bc its already proccessed blog part in main urls
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
#    path('user/<str:username>', UserProfileView.as_view(), name="user-profile"),
    #--------------------------------------------------------------------------------------------------------------------------------------
    #path('location/<str:loc>', LocationPostListView.as_view(), name="location-posts"),
   #--------------------------------------------------------------------------------------------------------------------------------------
    #path('', BootstrapFilterView, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#pk means primary key like post 1 post 2 etc
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about"),
    path('duyuru/', views.duyuru, name="blog-duyuru"),
#--------------------------------------------------------------------------------------------------------------------------------------
    path('tag/<slug:slug>/', TagIndexView.as_view(), name='tagged'),
    path('like/<int:pk>', LikeView, name='like_post'),
    #path('', BootstrapFilterView, name='bootstrap'),
    #path('tagy/<tags>', TagIndexView.as_view(), name="tagy-posts"),

#--------------------------------------------------------------------------------------------------------------------------------------
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]