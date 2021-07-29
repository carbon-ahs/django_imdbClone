from django.shortcuts import render

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from watchlist_app.models import WatchList, StreamPlatform, Reviwe
from watchlist_app.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchListSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviwe.objects.all()
    serializer_class = ReviewSerializer

class ReviewListCV(generics.ListAPIView):
    # queryset = Reviwe.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviwe.objects.filter(watchlist = pk)


class ReviewCreateCV(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Reviwe.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        reviw_user = self.request.user
        review_queryset = Reviwe.objects.filter(watchlist=watchlist, reviw_user=reviw_user)

        if review_queryset.exists():
            raise ValidationError('Already Reviewed Show!!!')

        serializer.save(watchlist = watchlist, reviw_user = reviw_user)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Reviwe.objects.all() 
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
        

class StreamPlatformListAV(APIView):
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platforms, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformAV(APIView):
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)

    def put(self, request, pk): 
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    
    
class AllWatchListAV(APIView):
    def get(self, request):
        try:
            all_watch_lists = WatchList.objects.all()
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(all_watch_lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class WatchListAV(APIView):
    def get(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watch_list)
        return Response(serializer.data)

    def put(self, request, pk): 
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watch_list, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        