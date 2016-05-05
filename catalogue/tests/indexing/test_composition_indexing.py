from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr

@override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
class TestCompositionIndexing(APITestCase):

    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['name'])
        q = self.server.search("*:*", fq=['type:composition', 'pk:{0}'.format(composition.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['name'])
        composition_pk = composition.pk
        params = {
            'fq': ['type:composition', 'pk:{0}'.format(composition_pk)]
        }
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits > 0)

        composition.delete()
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['name'])
        composition_pk = composition.pk
        fQ = ["type:composition", "pk:{0}".format(composition_pk)]
        server = pysolr.Solr(settings.SOLR['SERVER'])
        q = server.search("*:*", fq = fQ)
        self.assertTrue(q.hits > 0)

        composition.name = "Name1"
        composition.save()
        self.assertTrue(q.docs[0]['name_s'] == "Name1")


    def tearDown(self):
        pass

        #(line2) we do not want to put our garbage data (from model_mommy) with our good data (DIAMM data)