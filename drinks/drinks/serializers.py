from rest_framework import serializers
from .models import Drink
from .models import Bar

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
          model = Drink
          fields = ['id', 'name', 'description']


class BarSerializer(serializers.ModelSerializer):
     class Meta:
          model = Bar
          fields = ['id', 'name']