from django.contrib import admin
from . models import Orders


# Register your models here.

@admin.register(Orders)
class OdersAdmin(admin.ModelAdmin):
    list_display = ["topic", "pages", "subject","uploads"]




    