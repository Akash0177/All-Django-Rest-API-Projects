from rest_framework import serializers
class NameSerialzer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    
