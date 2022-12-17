# Generated by Django 4.1.4 on 2022-12-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0007_alter_membersimages_uploaded_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membersinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='memberssettings',
            name='id',
        ),
        migrations.AlterField(
            model_name='membersinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hello_world.members'),
        ),
        migrations.AlterField(
            model_name='memberssettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hello_world.members'),
        ),
    ]
