import csv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)

            for row in contents:
                print(row)