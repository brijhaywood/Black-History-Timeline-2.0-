from rest_framework import serializers
from facts.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'year', 'coord_v', 'coord_h', 'is_liked', 'has_viewed', 'category')
        model = Place