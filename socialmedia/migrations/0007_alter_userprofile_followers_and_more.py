# Generated by Django 4.2.7 on 2023-12-27 00:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialmedia', '0006_userprofile_followers_userprofile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
