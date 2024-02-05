from rest_framework import serializers
from .models import CustomUser, Coords, Post, Images


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['fam', 'name', 'otc', 'email', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    coords = serializers.PrimaryKeyRelatedField(queryset=Coords.objects.all())

    class Meta:
        model = Post
        fields = ("beauty_title",
                  "title",
                  "other_titles",
                  "connect",
                  "add_time",
                  "user",
                  "coords",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class AuthEmailPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("beauty_title",
                  "title",
                  "other_titles",
                  "connect",
                  "add_time",
                  "user",
                  "coords",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )
