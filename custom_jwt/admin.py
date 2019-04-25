from django.contrib import admin
from custom_jwt.models import BlackListedToken


class BlackListedTokenAdmin(admin.ModelAdmin):
    model = BlackListedToken
    list_display = ('user', 'timestamp', 'token')


admin.site.register(BlackListedToken, BlackListedTokenAdmin)
