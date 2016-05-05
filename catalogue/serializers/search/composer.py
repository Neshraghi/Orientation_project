from rest_framework import serializers
from catalogue.models.composer import Composer


class ComposerSearchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = ('pk', 'type', 'name_s')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    name_s = serializers.ReadOnlyField(source="name")

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()