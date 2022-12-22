from django.db import models


from django.contrib.auth.models import User
from django.db import models
from enum import IntEnum

from tinder_profile.models import Members

    
class ReactionType():
    LIKE = 1
    NO_MATCH = 2
    SUPER_LIKE = 3
    BLOCK = 4

# Create your models here.
class Reactions(models.Model):    
    reactor_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name='reactor')
    receiver_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name='receiver')
    issued_date = models.DateTimeField(auto_now_add=True)
    # remove reaction table
    type = models.IntegerField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['reactor_id', 'receiver_id'], name='unique_reactorid_receiverid_combination'
            )
        ]
    
    
class Connections(models.Model):
    user_id_1 = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name = 'user_id_1')
    user_id_2 = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name='user_id_2')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id_1', 'user_id_2'], name='unique_userid1_userid2_combination'
            )
        ]
    
    
class Messages(models.Model):
    """
    Model to represent user submitted changed to a resource guide
    """
    message_id = models.AutoField(primary_key=True)
    
    sender_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name='sender_id')    
    recipient_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False, related_name="recipent_id")
    
    message = models.TextField(null=False)
    send_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    

    def __str__(self):
        """
        String to represent the message
        """

        return self.message    
    


