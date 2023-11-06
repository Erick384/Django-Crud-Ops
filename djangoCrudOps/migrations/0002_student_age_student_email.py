# Generated by Django 4.2.7 on 2023-11-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoCrudOps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]