from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
            "tel_number",
        )

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except exceptions.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def validate(self, data):
        confirm_password = data.pop("confirm_password")
        if confirm_password != data.get("password"):
            raise ValidationError(
                "Passwords don't match. Make sure to enter same passwords"
            )
        return super().validate(data)

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserManageSerializer(serializers.ModelSerializer):
    country = serializers.CharField(max_length=65)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "favourites",
            "tel_number",
            "country",
            "city",
        )
        read_only_fields = ("id", "email")

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
