from django.urls import include, path
from rest_framework import routers

from content import views as content_views
from user import views as user_views

router = routers.DefaultRouter()
router.register("users", user_views.UserViewSet)
router.register("groups", user_views.GroupViewSet)
router.register("topics", content_views.TopicViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]