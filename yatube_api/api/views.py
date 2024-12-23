from rest_framework import viewsets  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore

from posts.models import Post, Comment, Group, Follow
from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)
from rest_framework.permissions import (  # type: ignore
    IsAuthenticatedOrReadOnly)
from .permissions import AuthorPermission  # type: ignore
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
from rest_framework import filters  # type: ignore
from rest_framework.pagination import LimitOffsetPagination  # type: ignore


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (AuthorPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    http_method_names = ['get']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
