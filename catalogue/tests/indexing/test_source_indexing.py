from rest_framework.test import APITestCase
from model_mommy import mommy


class TestSourceIndexing(APITestCase):
    def setup(self):
        pass

    def test_solr_index_on_create(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        #without _fill_optional, model_mommy is going to fill it with garbage (random things)
        self.assertIsNotNone(source)

    def test_solr_delete_on_delete(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        self.assertIsNotNone(source)

    def test_solr_index_onupdate(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        self.assertIsNotNone(source)

    def tearDown(self):
        pass