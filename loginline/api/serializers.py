from rest_framework import serializers
from loginline.models import UserLine

class UserLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserLine
        fields = "__all__"
