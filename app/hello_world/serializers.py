from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # get_username= serializers.Field()
    # get_big_picture= serializers.Field()
    # get_small_picture = serializers.Field()

    class Meta:
        model = Profile
        fields = (
            "get_username",
            "phone",
            "gender",
            "is_premium",
            "about_me",
            "birthday",
            "address",
            "get_big_picture",
            "get_small_picture"
        )