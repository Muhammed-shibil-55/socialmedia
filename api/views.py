from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions

from api.serializers import UserSerializer,ProfileSerializer,PostSerializer

from socialmedia.models import UserProfile,Posts

class SignUpView(APIView):
   def post(self,request,*args,**kwargs):
      serializer=UserSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(data=serializer.data)
      else:
         return Response(data=serializer.errors)
      
class ProfileView(viewsets.ViewSet):
   
   authentication_classes=[authentication.TokenAuthentication]
   permission_classes=[permissions.IsAuthenticated]

   def list(self,request,*args,**kwargs):
      qs=UserProfile.objects.get(user=request.user)
      serializer=ProfileSerializer(qs)
      return Response(data=serializer.data)
   
   def update(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      profile_obj=UserProfile.objects.get(id=id)
      serializer=ProfileSerializer(data=request.data,instance=profile_obj)
      if serializer.is_valid():
         serializer.save()
         return Response(data=serializer.data)
      else:
         return Response(data=serializer.errors)
      
class POstView(viewsets.ModelViewSet):
   serializer_class=PostSerializer
   queryset=Posts.objects.all()

   authentication_classes=[authentication.TokenAuthentication]
   permission_classes=[permissions.IsAuthenticated]

   def get_queryset(self):
      return Posts.objects.filter(user=self.request.user)
   
   def perform_create(self, serializer):
      serializer.save(user=self.request.user)