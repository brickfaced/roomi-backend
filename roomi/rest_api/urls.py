from django.urls import path
from rest_framework.authtoken import views
from .views import UserApi

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('user/', UserApi.as_view(), name='user-detail')
]
