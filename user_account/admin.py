from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'account_no', 'street1', 'street2', 'street3', 
        'town_city', 'post_code', 'country', 'phone', 'date_added',
        'date_removed', 'update_date',
    )

    ordering = ('id',)


admin.site.register(UserProfile, UserProfileAdmin)