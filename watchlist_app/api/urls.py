from django.urls import path, include
from watchlist_app.api import views


urlpatterns = [
    path('stream-platforms/', views.StreamPlatformListAV.as_view(), name='stream-platforms'),
    path('stream-platform/<int:pk>', views.StreamPlatformAV.as_view(), name='stream-platform'),
    path('all-watchlists/', views.AllWatchListAV.as_view(), name='all-watchlists'),
    
]