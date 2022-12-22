from io import BytesIO
from PIL import Image
# import Image
from django.db import models
from authentication.models import MyUser
from django.core.files import File

# Create your models here.

class Memberships(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    permissions = models.TextField(null=True)
    price= models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    enable = models.IntegerField(null=True)

    
class Members(models.Model):
    user = models.OneToOneField(MyUser, on_delete= models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    user_name = models.CharField(max_length = 1024, blank=True, null = True) # not null
    membership_date = models.DateField(auto_now=True)
    user_status = models.IntegerField(blank=True, null=True) # not null
    join_date = models.DateField(blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)
    approved_profile = models.IntegerField(null=True, blank=True)
    account_status = models.IntegerField(null=True, blank=True)

    group_id = models.ForeignKey(Memberships, on_delete=models.CASCADE, null=True) # not null



class MembersSettings(models.Model):
    user = models.OneToOneField(Members, on_delete= models.CASCADE, primary_key=True)
    search_locations = models.CharField(max_length=1024, blank=True, null=True)
    max_range = models.IntegerField(null=True, blank=True)
    min_match_age = models.IntegerField(null=True, blank=True)
    max_match_age = models.IntegerField(null=True, blank = True)
    visibility = models.IntegerField(null=True, blank = True)

class MembersInfo(models.Model):
    user = models.OneToOneField(Members, on_delete= models.CASCADE, primary_key=True)
    avatar_url =  models.ImageField(upload_to='uploads/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True,auto_now_add=True)
    gender = models.BooleanField(blank=True, null=True, default=False)
    address = models.CharField(max_length=1024, blank=True, null=True)
    street = models.CharField(max_length=1024, blank=True, null=True)
    district = models.CharField(max_length=1024, blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    country = models.CharField(max_length=1024, blank=True, null=True)
    language = models.CharField(max_length=1024, blank=True, null=True)
    hobby = models.CharField(max_length=1024, blank=True, null=True)
    company = models.CharField(max_length=1024, blank=True, null=True)
    school = models.CharField(max_length=1024, blank=True, null=True)

class MembersImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Members, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, max_length=1024)
    image_url = models.ImageField(upload_to='uploads/', blank=True, null=True)
    uploaded_date = models.DateField(blank=True, null=False, auto_now=True)

class Memberships(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    permissions = models.TextField(null=True)
    price= models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    enable = models.IntegerField(null=True)