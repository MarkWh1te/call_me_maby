from django.contrib import admin
from guardian.admin import GuardedModelAdmin
import models

# Register your models here.


class MenusAdmin(GuardedModelAdmin):
    pass

admin.site.register(models.Menus, MenusAdmin)
