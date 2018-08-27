from django.contrib import admin
from tiantianguaji.models import player,clear
# Register your models here.

#player模型的管理器
@admin.register(player)
class PlayerAdmin(admin.ModelAdmin):
    list=('usrid','id','hp','power')

#clear模型的管理器
@admin.register(clear)
class ClearAdmin(admin.ModelAdmin):
    list=('usrid','id','hp','power')