# Generated by Django 4.2.7 on 2024-01-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0008_alter_userprofile_bio_alter_userprofile_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profilpics'),
        ),
    ]