from io import BytesIO
from PIL import Image
# import Image
from django.db import models
from authentication.models import MyUser
from django.core.files import File
from django.utils import timezone


# Create your models here
class Memberships(models.Model):
    group_id = models.AutoField(primary_key=True)
    # 1 normal
    # 2 premium
    
    
    name = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    permissions = models.TextField(null=True)
    price= models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    # Number of time remaining for this service
    
    enable = models.IntegerField(null=True)
    def __str__(self):
        if self.group_id == 1:
            return "Normal User"
        else:
            return "Premium User"

class Members(models.Model):
    user = models.OneToOneField(MyUser, on_delete= models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    user_name = models.CharField(max_length = 1024, blank=True, null = True) # not null
    membership_date = models.DateField(blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True) # not null
    join_date = models.DateField(blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)
    approved_profile = models.IntegerField(null=True, blank=True)
    account_status = models.IntegerField(null=True, blank=True)

    group_id = models.ForeignKey(Memberships, on_delete=models.CASCADE, null=True,to_field='group_id', default = 1) # not null
    def __str__(self):
        return self.user.email

class AccountType:
    NORMAL = 1
    PREMIUM = 2
    
    @staticmethod
    def get_account_type(id):
        """ Returns account's type """
        member = Members.objects.get(user_id = id)

        if member.membership_date is None or timezone.now().date() > member.membership_date:
            return AccountType.NORMAL

        return AccountType.PREMIUM

class MembersSettings(models.Model):
    user = models.OneToOneField(Members, on_delete= models.CASCADE, primary_key=True)
    search_locations = models.CharField(max_length=1024, blank=True, null=True)
    max_range = models.IntegerField(null=True, blank=True)
    min_match_age = models.IntegerField(null=True, blank=True)
    max_match_age = models.IntegerField(null=True, blank = True)
    visibility = models.IntegerField(null=True, blank = True)
    def __str__(self):
        return self.user.user
    

class MembersInfo(models.Model):
    user = models.OneToOneField(Members, on_delete= models.CASCADE, primary_key=True)
    # avatar_url =  models.ImageField(upload_to='uploads/', blank=True, null=True)
    # header_url =  models.ImageField(upload_to='uploads/', blank=True, null=True)
    avatar_url = models.TextField(blank= True, null = True, max_length=1024)
    header_url = models.TextField(blank= True, null = True, max_length=1024)
    about_me = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True,auto_now_add=True)
    is_female = models.BooleanField(blank=True, null=True, default=False)
    address = models.CharField(max_length=1024, blank=True, null=True)
    street = models.CharField(max_length=1024, blank=True, null=True)
    district = models.CharField(max_length=1024, blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    country = models.CharField(max_length=1024, blank=True, null=True)
    language = models.CharField(max_length=1024, blank=True, null=True)
    hobby = models.CharField(max_length=1024, blank=True, null=True)
    company = models.CharField(max_length=1024, blank=True, null=True)
    school = models.CharField(max_length=1024, blank=True, null=True)
    def __str__(self):
        return self.user.user.email

    # def get_avatar_url(self):
    #     if(self.avatar_url):
    #         return 'http://127.0.0.1:8000'+self.avatar_url.url
    #     return ''
    # def get_header_url(self):
    #     if(self.header_url):
    #         return 'http://127.0.0.1:8000'+self.header_url.url
    #     return ''


    # def get_header_url(self):
    #     if(self.header_url):
    #         return self.header_url
    #     else:
    #         if self.avatar_url:
    #             self.header_url = self.make_header(self.avatar_url)
    #             self.save()

    #             return self.header_url
    #         else:
    #             return ''
    # def make_header(self, image, size = (300, 300)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     header_io = BytesIO()
    #     img.save(header_io, 'JPEG', quality = 85)

    #     header = File(header_io, name=image.name)
    #     return header


class MembersImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Members, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, max_length=1024)
    image_url = models.ImageField(upload_to='uploads/', blank=True, null=True)
    uploaded_date = models.DateField(blank=True, null=False, auto_now=True)

