from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField

class MachineModel(models.Model):
    product_no = models.CharField(max_length=200, primary_key=True)
    product_name = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    order_date =  models.DateTimeField()
    expected_arrival_date = models.DateTimeField()
    parts_used_to_make = HStoreField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.product_name

class MachinePart(models.Model):
    part_id_no = models.CharField(max_length=200, primary_key=True)
    quantity = models.IntegerField()
    suppliers = ArrayField(
            models.CharField(max_length=200)
        )