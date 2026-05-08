# serializers.py

from rest_framework import serializers
from .models import Person


# NORMAL SERIALIZER
class PersonSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        
        return instance


# MODEL SERIALIZER
class PersonModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'city']