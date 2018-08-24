from django.contrib import admin
from django.contrib import admin

from .models import (
    MachineModel, 
    MachinePart
)

@admin.register(MachineModel)
class MachineModelAdmin(admin.ModelAdmin):
    list_display = (
        'product_no', 
        'product_name',
        'stock_quantity',
        'order_date',
        'expected_arrival_date',
        'parts_used_to_make'
        )

@admin.register(MachinePart)
class MachinePartAdmin(admin.ModelAdmin):
    
    list_display = (
        'part_id_no',
        'quantity',
        'suppliers'
    )