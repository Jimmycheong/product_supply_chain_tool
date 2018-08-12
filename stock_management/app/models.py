from django.db import models

class MachineModel(models.Model):
    product_no = models.CharField(max_length=200)
    product_name = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    order_date =  models.DateTimeField()
    expected_arrival_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.product_name