from rest_framework import generics
from facts.models import Place
from .serializers import PlaceSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer