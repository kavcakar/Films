from rest_framework import serializers
from movieapp.models import Contain

class ContainSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    year = serializers.CharField()
    genre = serializers.CharField()
    director = serializers.CharField()
    aktif = serializers.BooleanField()
    writer = serializers.CharField()
    language = serializers.CharField()
    create_time = serializers.DateTimeField(read_only=True)
    updated_time =serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        return Contain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.director = validated_data.get('director', instance.director)
        instance.writer = validated_data.get('writer', instance.writer)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance
        