import csv
from django.core.management.base import BaseCommand
from catalogue.models.source import Source


class Command(BaseCommand):
    def _get_source(selfself, row):
        source, created = Source.objects.get_or_create(shelfmark=row['shelfMark'])
        #shelfMark is unique and it is always there, then it is a nice identifier

        if created:
            if row['sourceName']:
                source.name = row['sourceName']
                #it evaluates (null is false)
            if row['startdate']:
                source.start_date  = row['startdate']
            if row['enddate']:
                source.end_date = row['enddate']
            if row['sourceType']:
                source.type = row['sourceType']
            if row['dateComments']:
                source.comments = row['dateComments']
            if row['surface']:
                source.surface = row['surface']
            source.save()

        return source

    def handle(self, *args, **options):
        print('Deleting sources')
        Source.objects.all().delete()
        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)
            for row in contents:
                source = self._get_source(row)