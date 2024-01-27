from django.urls import path

from api import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("profile",views.ProfileView,basename="profile")

router1=DefaultRouter()
router1.register("posts",views.POstView,basename="posts")


urlpatterns=[
        path("register/",views.SignUpView.as_view()),
        path("token/",ObtainAuthToken.as_view()),
]+ router.urls + router1.urls