""" Django wait for database to be up and running
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django wait for database

    Args:
        BaseCommand (_type_): _description_
    """
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db..')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database down, waiting 1 second..')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database up and running!'))
