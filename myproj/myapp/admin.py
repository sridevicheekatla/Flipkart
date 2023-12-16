from django.contrib import admin

from myapp.models import (
    AllProducts,
    RegularFit,
    RelaxedFit
)


@admin.register(AllProducts)
class AllProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'active')
    list_filter = ('active',)


@admin.register(RegularFit)
class RegularFitAdmin(admin.ModelAdmin):
    list_display = ('id', 'fabric', 'ideal_for')


@admin.register(RelaxedFit)
class RelaxedFitAdmin(admin.ModelAdmin):
    list_display = ('id', 'fabric', 'ideal_for')
