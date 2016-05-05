from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr

@override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
class TestSourceIndexing(APITestCase):

    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        q = self.server.search("*:*", fq=['type:source', 'pk:{0}'.format(source.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        source_pk = source.pk
        params = {
            'fq': ['type:source', 'pk:{0}'.format(source_pk)]
        }
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits > 0)

        source.delete()
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        source_pk = source.pk
        fQ = ["type:source", "pk:{0}".format(source_pk)]
        #server = pysolr.Solr(settings.SOLR['SERVER']) NOT USEFUL, REDUNDANT, WE HAVE ALREADY DONE IT, ADD self IN NEXT LINE
        q = self.server.search("*:*", fq = fQ)
        #print(q.docs)
        self.assertTrue(q.hits > 0)

        source.name = "Name1"
        source.save()
        q = self.server.search("*:*", fq = fQ) # we were missing this search
        self.assertTrue(q.docs[0]['name_s'] == "Name1")


    def tearDown(self):
        pass

#(line2) we do not want to put our garbage data (from model_mommy) with our good data (DIAMM data)