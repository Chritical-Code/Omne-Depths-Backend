from django.urls import include, path
from rest_framework import routers

from content import views as content_views
from user import views as user_views

router = routers.DefaultRouter()
router.register("users", user_views.UserViewSet)
router.register("groups", user_views.GroupViewSet)
router.register("topics", content_views.TopicViewSet)
router.register("posts", content_views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]