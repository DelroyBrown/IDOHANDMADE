# idohandmade_markets/admin.py
from django.contrib import admin
from .models import MarketEvent, VendorApplication, EventDate


class EventDateInline(admin.TabularInline):
    model = EventDate
    extra = 1


class MarketEventAdmin(admin.ModelAdmin):
    inlines = [EventDateInline]


admin.site.register(MarketEvent, MarketEventAdmin)
admin.site.register(VendorApplication)
