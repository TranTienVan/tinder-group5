from rest_framework import serializers
from tinder.models import Reactions, Connections, Messages, Reports


        

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

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = (
            "report_id",
            "reporter_id",
            "violator_id",
            "type",
            "created_date",
            "description",
            "details_url",
            "status"
        )




