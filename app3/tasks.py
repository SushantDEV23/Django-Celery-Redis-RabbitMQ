from __future__ import absolute_import, unicode_literals
from celery import shared_task
import sys

from django.core.management import call_command

@shared_task(name='dbbackup')
def dbbackup():
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', 'app3')