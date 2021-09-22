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
            'admin_access',
            'portal_access',
            'settings_access',
            'accounts_access',
            'members_access',
            'committees_access',
            'dues_access',
            'executives_access',
            'action_plan_access',
            'budget_access',
            'attendance_access',
            'meetings_access',
            'groups_access',
            'year_access',
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
