from rest_framework import serializers
from movieapp.models import Contain

class ContainSerializer(serializers.ModelSerializer):
    time_since_pub =serializers.SerializerMethodField()
    class Meta:
        model = Contain
        fields = '__all__'
        # fields = ['title', 'year',]
        # exclude = ['title', 'year']
        read_only_fields = ['id', 'create_time', 'updated_time']

    def get_time_since_pub(self, object): 
        return 'Films'

class ContainDefaultSerializer(serializers.Serializer):
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


    def validate(self, data):
        if data ['director'] == data['writer']:
            raise serializers.ValidationError('it can not be same writer and director.')
        return data
        