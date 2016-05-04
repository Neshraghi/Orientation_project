import csv
from django.core.management.base import BaseCommand
from catalogue.models.source import Source
from catalogue.models.archive import Archive
from catalogue.models.composition import Composition
from catalogue.models.composer import Composer


class Command(BaseCommand):
    def _get_source(self, row):
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

    def _get_archive(self, row):
        archive, created = Archive.objects.get_or_create(name=row['archiveName'])

        if created:
            if row['archiveCity']:
                archive.city = row['archiveCity']
            if row['siglum']:
                archive.siglum = row['siglum']
            if row['archiveCountry']:
                archive.country = row['archiveCountry']
        return archive

    def _get_composer(self, row):
        composer, created = Composer.objects.get_or_create(name=row['composer'])
        return composer

    def _get_composition(self, row):
        composition, created = Composition.objects.get_or_create(title=row['composition_name'])
        return composition

    def handle(self, *args, **options):
        print('Deleting sources')
        Source.objects.all().delete()
        Archive.objects.all().delete()
        Composer.objects.all().delete()
        Composition.objects.all().delete()
        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)
            for rownum, row in enumerate(contents):
                print("importing row {0}".format(rownum))
                source = self._get_source(row)
                archive = self._get_archive(row)
                composition = self._get_composition(row)
                composer = self._get_composer(row)

                if not source.archive:
                    source.archive = archive
                    source.save()

                if not composition.composer:
                    composition.composer = composer
                    composition.save()

                if not composition.source:
                    composition.source = source
                    composition.save()

                if row['composer'] == 'no composer/anon':
                    composition.anonymous = True
                    composition.save()