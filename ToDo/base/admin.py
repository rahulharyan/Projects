from django.contrib import admin
from base.models import todoModel
from base.models import historyModel

# Register your models here.

class todoAdminModel(admin.ModelAdmin):
    list_display=['title','desc']

admin.site.register(todoModel,todoAdminModel)


class historyAdminModel(admin.ModelAdmin):
    list_display=['title','desc']

admin.site.register(historyModel,historyAdminModel)