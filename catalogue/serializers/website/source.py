from rest_framework import serializers
from catalogue.models.source import Source
from catalogue.models.archive import Archive


class SourceArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        # fields = ('url', 'pk', 'shelfmark')

    archive = SourceArchiveSerializer()