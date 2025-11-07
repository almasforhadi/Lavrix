from django.contrib import admin
from .models import SupportTicket, SupportResponse

class SupportResponseInline(admin.TabularInline):
    model = SupportResponse
    extra = 1

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'message', 'user__username')
    inlines = [SupportResponseInline]

@admin.register(SupportResponse)
class SupportResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'responder', 'created_at')
    search_fields = ('message', 'ticket__subject')
