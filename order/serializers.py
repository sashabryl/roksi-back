from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from order.models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    country = serializers.CharField(max_length=65)

    class Meta:
        model = Order
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "instagram",
            "phone_number",
            "country",
            "city",
        )

    def validate_country(self, value):
        """
        For easier integration with React. Accepts both keys and values of CODES_OF_COUNTRIES.
        """
        country_dict = settings.CODES_OF_COUNTRIES
        if value in list(country_dict.keys()):
            return value
        elif value in list(country_dict.values()):
            position = list(country_dict.values()).index(value)
            return list(country_dict.keys())[position]
        raise ValidationError(f"{value} is not a possible choice.")


class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "get_date",
            "product",
            "quantity",
            "calculate_total"
        )
