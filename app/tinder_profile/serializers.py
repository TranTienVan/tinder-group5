from rest_framework import serializers

from .models import  MembersInfo, MembersSettings, Members, Memberships

from django.utils import timezone

class MembersInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    group_id = serializers.SerializerMethodField()
    class Meta:
        model = MembersInfo
        # fields = '__all__'
        fields = (
            "user",
            "user_name",
            "avatar_url",
            "header_url",
            "about_me",
            "birthday",
            "is_female",
            "address",
            "street",
            "district",
            "city",
            "country",
            "language",
            "hobby",
            "company",
            "school",
            "group_id"
        )
        extra_kwargs = {'user': {'required': False}}
    
    def get_user_name(self, obj):
        return obj.user.user_name
    def get_group_id(self, obj):
        if obj.user.membership_date is None or timezone.now()> obj.user.membership_date:
            obj.user.group_id = Memberships.objects.get(group_id = 1)
        else:
            obj.user.group_id = Memberships.objects.get(group_id = 2)
        obj.user.save()
        return obj.user.group_id.group_id

        
class MembersSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersSettings
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class MembershipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memberships
        fields=(
            "group_id",
            "name",
            "description",
            "permissions",
            "price",
            "duration",
            "enable"
        )
    
    
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields=(
            "user_id",
            "email",
            "phone",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "about_me",
            "is_female",
            "group_id",
            "membership_date",
            "user_status",
            "join_date",
            "last_activity",
            "last_edit",
            "avatar_url",
            "get_header_url",
            "approved_profile",
            "account_status"
        )