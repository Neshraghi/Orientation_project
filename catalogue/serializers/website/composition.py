from rest_framework import serializers
from catalogue.models.composition import Composition


class CompositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composition