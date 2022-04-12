from django.shortcuts import render
from itsdangerous import serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsAdminOrReadOnly
from .models import News, Review
from .serializers import NewsSerializer, AddNewsSerializer, ReviewSerializer


class NewsList(ListCreateAPIView):
    queryset=News.objects.all()
    permission_classes=[IsAdminOrReadOnly]
    filter_backends=[SearchFilter, OrderingFilter,DjangoFilterBackend]
    pagination_class=PageNumberPagination
    ordering_fields=['publish']
    search_fields=['title','body']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddNewsSerializer
        return NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset=News.objects.all()
    serializer_class=AddNewsSerializer


class ReviewsList(ListCreateAPIView):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(news_id=self.kwargs['pk'])
    
    def get_serializer_context(self):
        return {'news_id':self.kwargs['pk']}

