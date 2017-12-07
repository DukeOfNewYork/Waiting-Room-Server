from django.contrib import admin
from .models import Computer


# Register your models here.


class ComputerAdmin(admin.ModelAdmin):
    readonly_fields = ('start_time',)
    list_display = ('name', 'start_time')


admin.site.register(Computer, ComputerAdmin)
