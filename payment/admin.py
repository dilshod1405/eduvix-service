from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'total_amount', 'status', 'created_at', 'method', 'id')
    list_filter = ('status', 'method')
    search_fields = ('user__username', 'module__name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    list_editable = ('status',)