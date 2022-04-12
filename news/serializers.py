from unicodedata import category
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News, Category, Review



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name']


class AddNewsSerializer(serializers.ModelSerializer):
    reporter_id=serializers.IntegerField()
    category_id=serializers.IntegerField()
    class Meta:
        model=News
        fields=['title','body','category_id','reporter_id']
    

class NewsSerializer(serializers.ModelSerializer):
    reporter=UserSerilaizer(read_only=True)
    category=CategorySerializer()
    class Meta:
        model=News
        fields=['id','title','body','category','reporter','publish']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['name','email','body','created']
    
    def create(self, validated_data):
        return Review.objects.create(news_id=self.context['news_id'], **validated_data)
    