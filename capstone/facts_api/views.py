from rest_framework import generics
from facts.models import Place
from .serializers import PlaceSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer