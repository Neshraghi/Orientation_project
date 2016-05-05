from rest_framework import serializers
from catalogue.models.archive import Archive


class ArchiveSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ('pk', 'type', 'name_s', 'city_s', 'siglum_s', 'country_s')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    name_s = serializers.ReadOnlyField(source="name")
    city_s = serializers.ReadOnlyField(source="city")
    siglum_s = serializers.ReadOnlyField(source="siglum")
    country_s =serializers.ReadOnlyField(source="country")

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()