from django.contrib import admin
from myapp.models import contact,Product,Category,Customer,Order
# Register your models here.
admin.site.register(contact)

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category']


class AdminCategory(admin.ModelAdmin):
	list_display = ['name']



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)