from django.db.models import fields
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Reviwe


class ReviewSerializer(serializers.ModelSerializer):
    reviwe_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Reviwe
        fields = '__all__'
        #exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True)    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
