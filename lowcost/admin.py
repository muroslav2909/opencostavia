# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lowcost.models import *
from django.contrib import admin

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Currency._meta.fields]
admin.site.register(Currency, CurrencyAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Country._meta.fields]
admin.site.register(Country, CountryAdmin)

class AirportAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Airport._meta.fields]
    list_filter = ['country',]
admin.site.register(Airport, AirportAdmin)

class FlightAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Flight._meta.fields]
admin.site.register(Flight, FlightAdmin)