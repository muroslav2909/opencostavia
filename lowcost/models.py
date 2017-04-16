# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal
from django.db import models
from lowcost.constants import MAIN_URL_WIZZAIR, COUNTRIES, PATH_TO_ITEMS
from lowcost.manager import setUp, set_departure, scroll, get_airports_list, clear_departure_airport, set_arrival, \
    button_click, show_time, get_normal_date


class Currency(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    code = models.CharField(max_length=32, null=True, blank=True)
    to_usd = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=4, default=0)
    to_hrn = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=4, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.code)


class Country(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    code = models.CharField(max_length=32)
    language_code = models.CharField(max_length=2, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)


class Airport(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    possible_way = models.ManyToManyField("self")
    code = models.CharField(max_length=32, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)

    def add_possible_way_wizzair(self):
        driver = setUp()
        driver.get(MAIN_URL_WIZZAIR)
        set_departure(driver, self.name)
        scroll(driver)
        result = get_airports_list(driver)
        for r in result:
            airport_name = u"%s" % r.rsplit(' ', 1)[0]
            if airport_name not in COUNTRIES:
                try:
                    self.possible_way.add(Airport.objects.get(name=airport_name))
                except Exception, e:
                    print e
        clear_departure_airport(driver)
        driver.quit()


    def add_flight(self):
        for possible_way in self.possible_way.all():
            driver = setUp()
            driver.get(MAIN_URL_WIZZAIR)
            set_departure(driver, self.name)
            set_arrival(driver, possible_way.name)
            button_click(driver)
            show_time(driver)
            for i in range(1, 36):
                path = PATH_TO_ITEMS % i
                if driver.find_element_by_xpath(path).text:
                    text = driver.find_element_by_xpath(path).text
                    info = text.split('\n')
                    if (i > 0 and i < 8 and int(info[0]) < 20) or (i > 28 and i < 37 and int(info[0]) > 20) or (i > 7 and i < 29):
                        date = get_normal_date(info[0], info[3])
                        curr = Currency.objects.get(code=info[2])
                        price_usd = Decimal(info[1]) * curr.to_usd
                        flight, create = Flight.objects.get_or_create(from_airport=self, to_airport=possible_way, date=date,
                                                                      defaults={'price': float(info[1]), 'currency': curr, 'price_usd': price_usd})
                        if not create:
                            Flight.objects.filter(from_airport=self, to_airport=possible_way, date=date).update(price=float(info[1]), currency=curr, price_usd=price_usd)
            driver.quit()


class Flight(models.Model):
    from_airport = models.ForeignKey(Airport, null=True, blank=True, default=None, related_name='flight_from_airport')
    to_airport = models.ForeignKey(Airport, null=True, blank=True, default=None, related_name='flight_to_airport')
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(null=False, blank=True, max_digits=10, decimal_places=4, default=0)
    currency = models.ForeignKey(Currency, null=True, blank=True, default=None)
    price_usd = models.DecimalField(null=False, blank=True, max_digits=10, decimal_places=4, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)


