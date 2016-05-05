from django.db.models import signals
from rest_framework.reverse import reverse
from catalogue.signals.composition_signals import index_composition
from catalogue.models.composition import Composition
from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


class CompositionViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_composition, sender=Composition)
        self.composition = mommy.make("catalogue.Composition")

    def test_fetches_html_detail_with_success(self):
        url = reverse('composition-detail', kwargs={"pk": self.composition.pk})
        response = self.client.get(url)
        #self.assertEqual(response.status.code, 200) #one way, or:
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_html_detail_with_failure(self):
        url = reverse('composition-detail', kwargs={"pk": 123456789})    #url = /composition/123456789/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass