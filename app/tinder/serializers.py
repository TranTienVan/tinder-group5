from rest_framework import serializers
from tinder.models import Members, Memberships, Reactions, Connections, Messages

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
            "gender",
            "group_id",
            "membership_date",
            "user_status",
            "join_date",
            "last_activity",
            "last_edit",
            "avatar_url",
            "approved_profile",
            "account_status"
        )
        

class ReactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactions
        fields = (
            "reactor_id",
            "receiver_id",
            "issued_date",
            "type"
        )
        


class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = (
            "user_id_1",
            "user_id_2",
            "created_date"
        )
    

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = (
            "message",
            "send_date",
            "status",
            "recipient_id",
            "sender_id"
        )



