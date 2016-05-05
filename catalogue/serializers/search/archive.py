from rest_framework import serializers
from catalogue.models.archive import Archive


class ArchiveSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ('pk', 'type', 'name_s', 'city_s', 'siglum_s', 'country_s')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    name_s = serializers.ReadOnlyField(archive="name")
    city_s = serializers.ReadOnlyField(archive="city")
    siglum_s = serializers.ReadOnlyField(archive="siglum")
    country_s =serializers.ReadOnlyField(archive="country")

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()