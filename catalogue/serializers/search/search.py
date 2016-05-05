from rest_framework import serializers
from catalogue.models.source import Source


class SourceSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('pk', 'type', 'shelfmark_s')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    shelfmark_s = serializers.ReadOnlyField(source="shelfmark")
    def get_type(self, obj):
        return self.Meta.model.__name__.lower()