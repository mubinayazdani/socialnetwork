from rest_framework.validators import UniqueValidator
from  django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]

    )
    password_1 =serializers.CharField(required=True, write_only=True)
    password_2 =serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password_1', 'password_2')


    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password': 'Password did not match.'
            })
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password_1']
        )

        return user