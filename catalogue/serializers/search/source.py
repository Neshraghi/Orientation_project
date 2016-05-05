from rest_framework import serializers
from catalogue.models.source import Source


class SourceSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('pk', 'type', 'shelfmark_s', 'name_s', 'start_date_i', 'end_date_i', 'type_s', 'surface_s', 'comments_s')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    shelfmark_s = serializers.ReadOnlyField(source="shelfmark")
    name_s = serializers.ReadOnlyField(source="name")
    start_date_i = serializers.ReadOnlyField(source="start_date")
    end_date_i = serializers.ReadOnlyField(source="end_date")
    type_s =serializers.ReadOnlyField(source="type")
    surface_s = serializers.ReadOnlyField(source="surface")
    comments_s = serializers.ReadOnlyField(source="comments")
    def get_type(self, obj):
        return self.Meta.model.__name__.lower()