from django.contrib import admin
import home.models as Models

# Register your models here.

# admin.site.register(tips)


class TipsTable(admin.ModelAdmin):
    list_display = ["writer", "name", "important"]


admin.site.register(Models.tips, TipsTable)


class NoticTable(admin.ModelAdmin):
    list_display = ["writer", "name", "important"]


admin.site.register(Models.notic, NoticTable)


class HerosTable(admin.ModelAdmin):
    list_display = ["SearchKey", "name"]


admin.site.register(Models.Heros, HerosTable)


class UserTable(admin.ModelAdmin):
    list_display = ["UID", "name"]


admin.site.register(Models.user, UserTable)


class BotSkillTable(admin.ModelAdmin):
    list_display = ["Skill"]


admin.site.register(Models.BotSkills, BotSkillTable)
