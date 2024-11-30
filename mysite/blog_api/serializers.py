from rest_framework import serializers
from mysite.blog.models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    body = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.body = validated_data.get('content', instance.body)
        instance.created = validated_data.get('created', instance.created)
        return instance