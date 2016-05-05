from django.db.models import signals
from rest_framework.reverse import reverse
from catalogue.signals.composer_signals import index_composer
from catalogue.models.composer import Composer
from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


class ComposerViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_composer, sender=Composer)
        self.composer = mommy.make("catalogue.Composer")

    def test_fetches_html_detail_with_success(self):
        url = reverse('composer-detail', kwargs={"pk": self.composer.pk})
        response = self.client.get(url)
        #self.assertEqual(response.status.code, 200) #one way, or:
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_html_detail_with_failure(self):
        url = reverse('composer-detail', kwargs={"pk": 123456789})    #url = /composer/123456789/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass