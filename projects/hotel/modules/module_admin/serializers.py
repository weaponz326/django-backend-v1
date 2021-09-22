from rest_framework import serializers
from .models import User, Access, Invitation

from accounts.serializers import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'updated_at',
            'account',
            'personal_id',
            'personal_name',
            'user_level',
        ]

# for getting accounts of a user
class UserAccountsSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'updated_at',
            'account',
            'personal_id',
            'personal_name',
            'user_level',
        ]

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = [
            'id',
            'updated_at',
            'admin_access',
            'portal_access',
            'settings_access',
            'bills_access',
            'staff_access',
            'guests_access',
            'roster_access',
            'payments_access',
            'services_access',
            'checkin_access',
            'bookings_access',
            'rooms_access',
            'assets_access',
            'housekeeping_access',
        ]

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            'id',
            'updated_at',
            'account',
            'invitee_id',
            'invitee_name',
            'invitation_status',
            'date_sent',
            'date_confirmed',
        ]
