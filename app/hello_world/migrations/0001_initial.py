# Generated by Django 4.1.3 on 2022-12-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('ClassId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_world.class')),
            ],
        ),
    ]