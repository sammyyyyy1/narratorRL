from rest_framework import serializers

from server.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ("id", "text")
