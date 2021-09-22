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
            'receivables_access',
            'products_access',
            'invoice_access',
            'marketting_access',
            'payables_access',
            'sales_access',
            'customers_access',
            'payments_access',
            'orders_access',
            'inventory_access',
            'suppliers_access',
            'purchasing_access',
            'cashflow_access',
            'staff_access',
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
