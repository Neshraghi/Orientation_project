from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr

@override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
class TestArchiveIndexing(APITestCase):

    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        q = self.server.search("*:*", fq=['type:archive', 'pk:{0}'.format(archive.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        archive_pk = archive.pk
        params = {
            'fq': ['type:archive', 'pk:{0}'.format(archive_pk)]
        }
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits > 0)

        archive.delete()
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        archive_pk = archive.pk
        fQ = ["type:archive", "pk:{0}".format(archive_pk)]
        #server = pysolr.Solr(settings.SOLR['SERVER']) NOT USEFUL, REDUNDANT, WE HAVE ALREADY DONE IT, ADD self IN NEXT LINE
        q = self.server.search("*:*", fq = fQ)
        self.assertTrue(q.hits > 0)

        archive.name = "Name1"
        archive.save()
        self.assertTrue(q.docs[0]['name_s'] == "Name1")

    def tearDown(self):
        pass

        #(line2) we do not want to put our garbage data (from model_mommy) with our good data (DIAMM data)