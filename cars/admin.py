from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price')
    search_fields = ('brand', 'model')
    list_filter = ('year',)
