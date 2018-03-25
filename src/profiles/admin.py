from django.contrib import admin

# Register your models here.
from .models import UserProfile


class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile


admin.site.register(UserProfile, profileAdmin)
