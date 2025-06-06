

from django.contrib import admin
from .models import Herb,ContactMessage

admin.site.register(Herb)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','created_at')
    search_fields = ('name', 'email', 'message')
# Register your models here.
