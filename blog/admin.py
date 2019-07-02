from django.contrib import admin

from .models import Post, Forced, Period

class ChoiceInline(admin.TabularInline):
    model = Forced
    extra = 4

class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pay_period']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Post)
#admin.site.register(Forced)
admin.site.register(Period, PeriodAdmin)
