from django.contrib import admin

# Register your models here.
from .models import Product, ProductRating, MyProducts, Thumbnail
from .models import (
    Product,
    ProductRating,
    MyProducts,
    Thumbnail,
    CuratedProducts
)

class ThumbnailInline(admin.TabularInline):
    extra = 1
    model = Thumbnail

class ProductAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ["__unicode__", "description", "price", "sale_price"]
    list_filter = ["price", "sale_price"]
    search_fields = ["title", "description"]
    list_editable = ["sale_price"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRating)
admin.site.register(MyProducts)
admin.site.register(Thumbnail)
admin.site.register(CuratedProducts)