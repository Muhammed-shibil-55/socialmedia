# Generated by Django 4.2.7 on 2024-01-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0010_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='𝘈 𝘷 𝘢 𝘵 𝘢 𝘳 ᥫ᭡ -.jpeg', upload_to='profilpics'),
        ),
    ]
