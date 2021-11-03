from django.contrib import admin
from .models import Quote
# Register your models here.
@admin.register(Quote)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quote']