from rest_framework import serializers

from .models import ExtendedProfile


class ExtendedProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedProfile
        fields = [
            'id',
            'updated_at',
            'date_of_birth',
            'gender',
            'country',
            'state',
            'city',
            'phone',
            'address',
        ]
