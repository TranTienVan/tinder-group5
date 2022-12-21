from io import BytesIO
from PIL import Image
# import Image
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    is_premium = models.BooleanField(blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_reported = models.BooleanField(blank=True, null=True)
    is_blocked = models.BooleanField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    gender = models.BooleanField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    big_picture_url = models.ImageField(upload_to='uploads/', blank=True, null=True)
    small_picture_url = models.ImageField(upload_to='uploads/', blank=True, null=True)
    country = models.CharField(max_length=1024, blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    district = models.CharField(max_length=1024, blank=True, null=True)
    street = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    school = models.CharField(max_length=1024, blank=True, null=True)

    # class Meta:
    #     managed = True
    #     db_table = 'hello_world_profile'
    
    def get_username (self):
        return self.user.username
    
    def get_big_picture(self):
        if self.big_picture_url:
            return 'http://localhost:8000' + self.big_picture_url.url
        else:
           return ''
  
    def get_small_picture(self):
        if self.small_picture_url:
            return 'http://localhost:8000' + self.small_picture_url.url
        else:
            if self.big_picture_url:
                self.small_picture_url = self.make_small_picture(self.big_picture_url)
                self.save()

                return 'http://localhost:8000' + self.small_picture_url
            else:
                return ''
    def make_small_picture(self, image, size = (300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality = 85)

        small_picture_url =  File(thum_io, name = image.name)
        return small_picture_url





class Members(models.Model):
    user_id =models.AutoField(primary_key=True)
    email = models.CharField(max_length=1024, blank=True, null=False, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=1024, blank=True, null = False)
    user_name = models.CharField(max_length = 1024, blank=True, null = False)
    group_id = models.IntegerField(blank=True, null= False)
    membership_date = models.DateTimeField(blank= True, null= True)
    user_status = models.IntegerField(blank=True, null=False)
    join_date = models.DateField(blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)
    approved_profile = models.IntegerField(null=True, blank=True)
    account_status = models.IntegerField(null=True, blank=True)



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

