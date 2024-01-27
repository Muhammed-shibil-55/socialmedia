from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True,blank=True)
    post_image=models.ImageField(upload_to="post-images")
    created_date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title
    
class UserProfile(models.Model):
    profile_picture=models.ImageField(upload_to="profilpics",default="default.jpeg")
    bio=models.CharField(max_length=600,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    liked_posts=models.ManyToManyField(Posts,null=True,related_name="liked_post")
    following=models.ManyToManyField(User,related_name="following",null=True)
    followers=models.ManyToManyField(User,related_name="followers",null=True)

    def __str__(self) -> str:
        return self.user.username
    
    @property
    def all_posts(self):
        qs=Posts.objects.filter(user=self.user)
        return qs
    


    


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.text


class Stories(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    picture=models.ImageField(upload_to="storiesimages")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Likes(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="post")
    liked_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")


def user_created(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(user_created,sender=User)