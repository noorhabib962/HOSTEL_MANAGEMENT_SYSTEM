from django.contrib import admin
from django.utils.html import format_html
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'month', 'student')


admin.site.register(Payment,PaymentAdmin)




