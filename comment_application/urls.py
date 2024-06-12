from django.urls import path
from comment_application.views import CommentListCreate, CommentDetail

urlpatterns = [
    path('', CommentListCreate.as_view(), name='comment-list-create'),
    path('<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
