from rest_framework import serializers
from myapp.models import transaction


class myappSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'