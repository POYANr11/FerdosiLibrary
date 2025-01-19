from django.urls import include, path
from .views import *

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('toggle-like-dislike/', ToggleLikeDislikeView.as_view(), name='toggle_like_dislike'),
]
