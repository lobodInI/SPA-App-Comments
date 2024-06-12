from rest_framework import serializers
from comment_application.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'username', 'email', 'home_page',
            'text', 'parent', 'created_at', 'replies'
        ]

    def get_replies(self, obj) -> dict | None:
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return None
