from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
router = DefaultRouter()
router.register(r'singer', SingerView, basename='singer')
router.register(r'song', SongView, basename='song')

urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verifytoken'),
    ] +router.urls