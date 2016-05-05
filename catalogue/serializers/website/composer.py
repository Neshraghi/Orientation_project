from rest_framework import serializers
from catalogue.models.composer import Composer


class ComposerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composer