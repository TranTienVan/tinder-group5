# Generated by Django 4.1.4 on 2022-12-07 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewClass',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='ClassId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_world.newclass'),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]