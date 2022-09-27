from coping_app.models.user import CustomUser
from coping_app.models.internship import Internship
from coping_app.models.company import Company
from coping_app.models.post import Post
from coping_app.models.comment import Comment
from coping_app.serializers import UserSerializer, InternshipSerializer, CompanySerializer, PostSerializer, CommentSerializer
from coping_app.permissions import IsOwnerOrReadOnly
# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer) -> None:
        serializer.save(onwer=self.request.user)


class CommentViewSet(viewsets.Mode):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer) -> None:
        serializer.save(onwer=self.request.user)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'internships': reverse('internship-list', request=request, format=format)
    })
