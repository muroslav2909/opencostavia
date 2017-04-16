from __future__ import absolute_import
from celery.task import periodic_task, task
from lowcost.models import *

@task()
def task_add_flight(airport_id):
    try:
        Airport.objects.get(id=airport_id).add_flight()
    except Exception, e:
        print e

@task()
def task_add_possible_way_wizzair(airport_id):
    try:
        Airport.objects.get(id=airport_id).add_possible_way_wizzair()
    except Exception, e:
        print e