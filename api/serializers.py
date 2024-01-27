from rest_framework import serializers

from django.contrib.auth.models import User

from socialmedia.models import UserProfile,Posts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","first_name","last_name","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class PostSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Posts
        fields="__all__"
        read_only_fields=["id","user","created_date"]


class ProfileSerializer(serializers.ModelSerializer):
    all_posts=PostSerializer(read_only=True,many=True)
    user=serializers.StringRelatedField()
    following=serializers.StringRelatedField(many=True)
    followers=serializers.StringRelatedField(many=True)
    class Meta:
        model=UserProfile
        fields=["profile_picture","bio","dob","phone","user","liked_posts","following","followers","all_posts"]
        read_only_fields=["id","user","liked_posts"," following","followers","all_posts"]


