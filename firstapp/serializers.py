from rest_framework import serializers
from .models import Note,Book,Standard,Students


class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Standard
        fields="__all__"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"