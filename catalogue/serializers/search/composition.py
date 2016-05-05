from rest_framework import serializers
from catalogue.models.composition import Composition


class CompositionSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = ('pk', 'type', 'title_s', 'anonymous_b')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    title_s = serializers.ReadOnlyField(source="title")
    anonymous_b = serializers.ReadOnlyField(source="anonymous")

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()