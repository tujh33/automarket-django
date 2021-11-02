from django.contrib import admin
from .models import *

# Register your models here.

class AutosAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','city','year','engine', 'color', 'gear', 'transmission', 'bodytype','created_at')

admin.site.register(Autos, AutosAdmin)
admin.site.register(Colors)
admin.site.register(Gears)
admin.site.register(Transmissions)
admin.site.register(Bodytypes)
admin.site.register(Rudders)