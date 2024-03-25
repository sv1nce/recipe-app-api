import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for Database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                # Try to access the default database
                connection = connections['default']
                connection.ensure_connection()
                db_up = True
            except OperationalError:
                # If connection fails, wait and try again
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))

