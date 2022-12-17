# Generated by Django 4.1.4 on 2022-12-14 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=1024)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('password', models.CharField(blank=True, max_length=1024)),
                ('first_name', models.CharField(blank=True, max_length=1024)),
                ('last_name', models.CharField(blank=True, max_length=1024)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True)),
                ('gender', models.BooleanField(blank=True)),
                ('group_id', models.IntegerField(blank=True)),
                ('membership_date', models.DateTimeField(auto_now=True)),
                ('user_status', models.IntegerField(blank=True)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('avatar_url', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('approved_profile', models.IntegerField(blank=True, null=True)),
                ('account_status', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembersSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_locations', models.CharField(blank=True, max_length=1024, null=True)),
                ('max_range', models.IntegerField(blank=True, null=True)),
                ('min_match_age', models.IntegerField(blank=True, null=True)),
                ('max_match_age', models.IntegerField(blank=True, null=True)),
                ('visibility', models.IntegerField(blank=True, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hello_world.members')),
            ],
        ),
        migrations.CreateModel(
            name='MembersInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('street', models.CharField(blank=True, max_length=1024, null=True)),
                ('district', models.CharField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(blank=True, max_length=1024, null=True)),
                ('country', models.CharField(blank=True, max_length=1024, null=True)),
                ('language', models.CharField(blank=True, max_length=1024, null=True)),
                ('hobby', models.CharField(blank=True, max_length=1024, null=True)),
                ('company', models.CharField(blank=True, max_length=1024, null=True)),
                ('school', models.CharField(blank=True, max_length=1024, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hello_world.members')),
            ],
        ),
        migrations.CreateModel(
            name='MembersImages',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, max_length=1024)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('uploaded_date', models.DateField(blank=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hello_world.members')),
            ],
        ),
    ]