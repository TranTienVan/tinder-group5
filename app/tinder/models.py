from django.db import models


from django.contrib.auth.models import User
from django.db import models






class Memberships(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    permissions = models.TextField(null=True)
    price= models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    enable = models.IntegerField(null=True)
    

class Members(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024)
    password = models.CharField(max_length=1024)
    first_name = models.CharField(max_length=1024, null=True)
    last_name = models.CharField(max_length=1024, null=True)
    birth_date = models.DateField(null=True)
    about_me = models.TextField(null=True)
    gender = models.IntegerField(null=True)
    membership_date = models.DateTimeField(null=True)
    user_status = models.IntegerField(null=True)
    join_date = models.DateTimeField(null=True)
    last_activity = models.DateTimeField(null=True)
    last_edit = models.DateTimeField(null=True)
    avatar_url = models.CharField(max_length=1024, null=True)
    approved_profile = models.IntegerField(null=True)
    account_status = models.IntegerField(null=True)
    
    group_id = models.ForeignKey(Memberships, on_delete=models.CASCADE, null=False)
    

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
    


