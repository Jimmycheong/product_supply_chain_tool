from rest_framework import serializers
from app.models import MachineModel


class MachineModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_no = serializers.CharField(required=False, allow_blank=True, max_length=100)
    product_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    stock_quantity = serializers.IntegerField(required=False)
    order_date = serializers.DateTimeField()
    expected_arrival_date = serializers.DateTimeField()
    parts_used_to_make = serializers.HStoreField(child=serializers.CharField(max_length=100))
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return MachineModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.product_no = validated_data.get('product_no', instance.product_no)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.expected_arrival_date = validated_data.get('expected_arrival_date', instance.expected_arrival_date)
        instance.save()
        return instance

class MachinePartSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    part_id_no = serializers.CharField(required=False, allow_blank=True, max_length=100)
    quantity = serializers.IntegerField(required=False)
    suppliers = serializers.ListField(
        child = serializers.CharField(required=False, allow_blank=True, max_length=100)
    )
