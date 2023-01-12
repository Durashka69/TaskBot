from django.urls import path

from rest_framework.routers import DefaultRouter

from main.views import UserRegisterView, PostViewSet, LikeView


router = DefaultRouter()

router.register("posts", PostViewSet)


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_creation"),
    path("likes/", LikeView.as_view(), name="likes_creation"),
]

urlpatterns += router.urls
