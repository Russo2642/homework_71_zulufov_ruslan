from api.views import PostView, LikeView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostView)
router.register('likes', LikeView)

urlpatterns = [
    path('', include(router.urls)),
]
