from django.contrib import admin
from apps.shop.models import *
from mptt.admin import DraggableMPTTAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms


class CategoryAdmin(DraggableMPTTAdmin):
    pass

class ProductAdminCkeditor(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductImagesInline(admin.TabularInline):
    model = ImagesForProducts
    extra: 4

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'price', 'image_tag', 'category', 'id')
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImagesInline,]
    form = ProductAdminCkeditor

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag')
    list_filter = ['product']
    
admin.site.register(ImagesForProducts, ImagesAdmin)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)