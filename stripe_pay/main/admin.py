from django.contrib import admin
from .models import Item, Order, Discount, Tax, Currency


class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'order_price', 'discount', 'tax', 'currency',)
    list_display_links = ('id', 'order_price',)
    # пагинация - по 10 записей на страницу
    list_per_page = 10
    # сколько можно максимально показать при нажатии кнопки show all
    list_max_show_all = 100
    # how to show empty values
    empty_value_display = '-empty-'
    # То что будет видно при переходе в каждую запись
    fields = ('id', 'item', 'order_price', 'discount', 'tax',  'currency',)
    readonly_fields = ('id',)


class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tax_size')
    list_display_links = ('name',)
    list_per_page = 10
    empty_value_display = '-empty-'
    fields = ('id', 'name', 'tax_size')
    readonly_fields = ('id',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discount')
    list_display_links = ('name',)
    list_per_page = 10
    empty_value_display = '-empty-'
    fields = ('id', 'name', 'discount')
    readonly_fields = ('id',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'price',)
    list_display_links = ('name',)
    list_per_page = 10
    empty_value_display = '-empty-'
    fields = ('id', 'name', 'description', 'price', )
    readonly_fields = ('id',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Currency, )
