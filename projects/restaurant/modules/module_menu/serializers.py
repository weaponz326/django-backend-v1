from rest_framework import serializers

from .models import MenuGroup, MenuItem


class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroup
        fields = [
            'id',
            'updated_at',
            'account',
            'menu_group',
            'category',
        ]

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id',
            'updated_at',
            'menu_group',
            'item_code',
            'item_name',
            'price',
            'description',
        ]


    def __init__(self, *args, **kwargs):
        super(MenuItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
