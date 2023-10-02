from rest_framework import serializers

from bulletin_board_app.models import Advert, Category, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdvertListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # or serializers.CharField(source='category.name')
    city = CitySerializer()  # or serializers.CharField(source='city.name')

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # or serializers.CharField(source='category.name')
    city = CitySerializer()  # or serializers.CharField(source='city.name')

    class Meta:
        model = Advert
        fields = '__all__'

