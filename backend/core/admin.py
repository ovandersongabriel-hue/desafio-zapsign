from django.contrib import admin
from .models import Company, Document, Signer

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'last_updated_at')
    search_fields = ('name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'open_id', 'status', 'company', 'created_at')
    list_filter = ('status', 'company')
    search_fields = ('name', 'open_id')

@admin.register(Signer)
class SignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'document')
    list_filter = ('status',)
    search_fields = ('name', 'email')