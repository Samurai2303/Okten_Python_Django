import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for connection...')
        db_con = False

        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database is unavailable')
                time.sleep(1)

        self.stdout.write('Database is available')
