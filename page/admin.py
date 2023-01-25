from django.contrib import admin
from page.models import Product,Cart,CartProduct
# # Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display=['title','price']
#     list_filter= ['category']
#     list_display_links = ['title']
    
#     class Meta:
        
#         model = Product
    
# admin.site.register(Product, ProductAdmin)

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)