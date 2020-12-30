from rest_framework import viewsets
from .serializers import PostSerializer
from .models import PostModel
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F


class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.order_by('-post_time').all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        vote = PostModel.objects.get(id=pk)
        vote.up_votes = vote.up_votes + 1
        vote.save()
        return Response({'status': 'ok'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        vote = PostModel.objects.get(id=pk)
        vote.down_votes = vote.down_votes + 1
        vote.save()
        return Response({'status': 'ok'})

    @action(detail=False)
    def sorted_votes(self, request):
        votes = PostModel.objects.annotate(
            score=F('up_votes') - F('down_votes')).order_by('-score')
        serializer = self.get_serializer(votes, many=True)
        return Response(serializer.data)

    # @action(detail=False)
    def get_post(self, request, secret_key):
        secret = PostModel.objects.get(secret_key=secret_key)
        serializer = PostSerializer(secret, many=False)
        return Response(serializer.data)
