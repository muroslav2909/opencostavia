# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lowcost.models import *
from django.contrib import admin
from lowcost.tasks import *

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Currency._meta.fields]
admin.site.register(Currency, CurrencyAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Country._meta.fields]
admin.site.register(Country, CountryAdmin)

class AirportAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Airport._meta.fields]
    list_filter = ['country',]
    actions = ('add_flight', 'add_possible_way_wizzair')

    def add_flight(self, request, queryset):
        for airport in queryset:
            task_add_flight.delay(airport.id)

    def add_possible_way_wizzair(self, request, queryset):
        for airport in queryset:
            task_add_possible_way_wizzair.delay(airport.id)


admin.site.register(Airport, AirportAdmin)

class FlightAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Flight._meta.fields]

admin.site.register(Flight, FlightAdmin)