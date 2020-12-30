from rest_framework import serializers
from .models import PostModel


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', 'isBoast', 'post', 'up_votes',
                  'down_votes', 'post_time', 'secret_key']
