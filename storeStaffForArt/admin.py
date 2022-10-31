from django.contrib import admin
from .models import productForArt,typeProductForArt,albomForArt,paintForArt,brashForArt
from django.utils.safestring import mark_safe
@admin.register(productForArt)
class productForArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','type','image_show']
    def image_show(self, obj):
        if obj.pictureProductForArt:
            return mark_safe("<img src='{}' width=30 />".format(obj.pictureProductForArt.url))
        return 'None'
    image_show.__name__='картинка'

admin.site.register(typeProductForArt)
@admin.register(albomForArt)
class albomForArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','numberOfPages']
@admin.register(paintForArt)
class paintForArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','typePaint','volumePaint']
    list_filter = ['typePaint']
@admin.register(brashForArt)
class brashForArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','typeMaterialBrash','volumeBrash']
    list_filter = ['typeMaterialBrash']

# Register your models here.
