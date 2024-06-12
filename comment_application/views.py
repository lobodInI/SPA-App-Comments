from django.db.models import QuerySet
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from comment_application.models import Comment
from comment_application.serializers import CommentSerializer


class OrderPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["username", "email", "created_at"]
    ordering = ["-created_at"]
    pagination_class = OrderPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        return Comment.objects.filter(parent__isnull=True)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (IsAuthenticated,)
