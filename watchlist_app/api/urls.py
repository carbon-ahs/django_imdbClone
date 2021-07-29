from django.db import router
from django.urls import path, include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('', include(router.urls)),

    path('stream-platforms/', views.StreamPlatformListAV.as_view(), name='stream-platforms'),
    path('stream-platform/<int:pk>', views.StreamPlatformAV.as_view(), name='stream-platform'),
    path('watchlists/', views.AllWatchListAV.as_view(), name='watchlists'),
    path('watchlist/<int:pk>', views.WatchListAV.as_view(), name='watchlist'),
    
    # i messed up here

    # path('reviewlist/', views.ReviewList.as_view(), name='reviewlist'),
    # path('reviewdetail/<int:pk>', views.ReviewDetail.as_view(), name='review'),
    path('watchlist/<int:pk>/reviewlist/', views.ReviewListCV.as_view(), name='reviewlist'),
    path('watchlist/<int:pk>/review-create/', views.ReviewCreateCV.as_view(), name='review'),

] 