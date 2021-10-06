from rest_framework import serializers

from .models import (
    Roster,
    RosterSheet,
    Shift,
    Batch,
    StaffPersonnel,
    RosterDay
)
from modules.module_staff.serializers import StaffListSerializer

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = [
            'id',
            'updated_at',
            'account',
            'roster_code',
            'roster_name',
            'from_date',
            'to_date',
        ]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'id',
            'updated_at',
            'roster',
            'shift_name',
            'start_time',
            'end_time',
        ]

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id',
            'updated_at',
            'roster',
            'batch_name',
            'batch_symbol',
        ]

class StaffPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPersonnel
        fields = [
            'id',
            'updated_at',
            'roster',
            'staff',
            'batch',
        ]

class StaffPersonnelListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    staff = StaffListSerializer()

    class Meta:
        model = StaffPersonnel
        fields = [
            'id',
            'updated_at',
            'roster',
            'staff',
            'batch',
        ]
        depth = 1

class RosterDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterDay
        fields = [
            'id',
            'updated_at',
            'roster',
            'day',
        ]

class RosterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterSheet
        fields = '__all__'
        fields = [
            'id',
            'updated_at',
            'roster_day',
            'shift',
            'batch',
        ]
