from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr

@override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
class TestComposerIndexing(APITestCase):

    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        composer = mommy.make("catalogue.Composer", _fill_optional=['name'])
        q = self.server.search("*:*", fq=['type:composer', 'pk:{0}'.format(composer.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        composer = mommy.make("catalogue.Composer", _fill_optional=['name'])
        composer_pk = composer.pk
        params = {
            'fq': ['type:composer', 'pk:{0}'.format(composer_pk)]
        }
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits > 0)

        composer.delete()
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        composer = mommy.make("catalogue.Composer", _fill_optional=['name'])
        composer_pk = composer.pk
        fQ = ["type:composer", "pk:{0}".format(composer_pk)]
        #server = pysolr.Solr(settings.SOLR['SERVER']) NOT USEFUL, REDUNDANT, WE HAVE ALREADY DONE IT, ADD self IN NEXT LINE
        q = self.server.search("*:*", fq = fQ)
        self.assertTrue(q.hits > 0)

        composer.name = "Name1"
        composer.save()
        q = self.server.search("*:*", fq = fQ) # we were missing this search
        self.assertTrue(q.docs[0]['name_s'] == "Name1")


    def tearDown(self):
        pass

        #(line2) we do not want to put our garbage data (from model_mommy) with our good data (DIAMM data)