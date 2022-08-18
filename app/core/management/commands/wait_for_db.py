"""
Django cmd to wait for db to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Waits for db to start."""

    def handle(self, *args, **options):
        pass
