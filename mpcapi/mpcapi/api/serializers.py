from rest_framework import serializers
from models import Post,Comment

class SerializeComment(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'postId', 'name', 'email', 'body')

class SerializePost(serializers.ModelSerializer):
    #comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment_list')
    #comments = SerializeComment(read_only=True)
    #comments = serializers.SerializerMethodField('get_comments')

    #def get_comments(self, obj):
    #    return "http://127.0.0.1:8000/comments_from_post/%d/" % obj.id

    class Meta:
        model = Post
        fields = ('id', 'userId', 'title', 'body')#, 'comments')

