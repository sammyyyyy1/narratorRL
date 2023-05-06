from rest_framework import serializers

from server.models import ImageText


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageText
        fields = ("id", "text")
