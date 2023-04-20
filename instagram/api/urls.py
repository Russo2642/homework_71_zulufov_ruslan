from api.views import PostView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostView)

urlpatterns = [
    path('', include(router.urls)),
]
