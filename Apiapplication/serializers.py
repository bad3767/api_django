from rest_framework import serializers

class Bookserializer(serializers.serializers):
    id=serializers.IntegerField(Label="Enter Book ID")
    title=serializers.CharField(Label="Enter Book title")
    author=serializers.CharField(Label="Enter Book Author")