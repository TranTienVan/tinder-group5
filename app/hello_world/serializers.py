from rest_framework import serializers

from .models import  MembersInfo, MembersSettings

class MembersInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = MembersInfo
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
    
    def get_user_name(self, obj):
        return obj.user.user_name

class MembersSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersSettings
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
