from django.contrib import admin
from .models import Product, Category, Supply, Descent, Delivery_memory, Descent_memory

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'kind','category' ]
    list_filter = ['name', 'kind', 'category']
    autocomplete_fields = ['category']
    search_fields = ['name']
    list_select_related = True

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class Supply_memoryInline(admin.TabularInline):
    model = Delivery_memory 
    extra = 1  

class SupplyAdmin(admin.ModelAdmin):
    date_hierarchy = "supply_date"
    list_display = ['supply_date']
    search_fields = ['products']
    autocomplete_fields = ['products']
    inlines = (Supply_memoryInline,)

class Descent_memoryInline(admin.TabularInline):
    model = Descent_memory
    extra = 1  

class DescentAdmin(admin.ModelAdmin):
    date_hierarchy = "descent_date"
    list_display = ['descent_date']
    search_fields = ['products']
    autocomplete_fields = ['products']
    inlines = (Descent_memoryInline,)

class Delivery_memoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'supply', 'quantity']
    list_filter = ['product', 'supply']
    autocomplete_fields = ['product', 'supply']
 

class Descent_memoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'descent', 'quantity']
    list_filter = ['product', 'descent']
    autocomplete_fields = ['product', 'descent']
    




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Descent, DescentAdmin)
admin.site.register(Delivery_memory, Delivery_memoryAdmin)
admin.site.register(Descent_memory, Descent_memoryAdmin)



