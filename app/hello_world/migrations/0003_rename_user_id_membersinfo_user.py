# Generated by Django 4.1.4 on 2022-12-14 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0002_members_memberssettings_membersinfo_membersimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membersinfo',
            old_name='user_id',
            new_name='user',
        ),
    ]
