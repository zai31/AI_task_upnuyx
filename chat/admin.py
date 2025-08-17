from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Chat


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'get_email', 'tokens', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Tokens'), {'fields': ('tokens',)}),
    )
    
    def get_email(self, obj):
        return obj.email
    get_email.short_description = 'Email'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'tokens', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_preview', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('message', 'response', 'user__username')
    readonly_fields = ('timestamp',)
    
    def message_preview(self, obj):
        return f"{obj.message[:50]}..." if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message Preview'


admin.site.register(User, CustomUserAdmin)
admin.site.register(Chat, ChatAdmin)
