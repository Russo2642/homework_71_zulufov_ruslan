from accounts.views import (
    LoginView,
    RegisterView,
    logout_view,
    ProfileView,
    UserChangeView,
    follow,
    SubscribersView,
    SubscriptionsView
)
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('profile/<int:pk>/follow', follow, name='follow'),
    path('profile/<int:pk>/subscribers/', SubscribersView.as_view(), name='subscribers'),
    path('profile/<int:pk>/subscriptions/', SubscriptionsView.as_view(), name='subscriptions')
]
