from django.db.models import signals
from rest_framework.reverse import reverse
from catalogue.signals.archive_signals import index_archive
from catalogue.models.archive import Archive
from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


class ArchiveViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_archive, sender=Archive)
        self.archive = mommy.make("catalogue.Archive")

    def test_fetches_html_detail_with_success(self):
        url = reverse('archive-detail', kwargs={"pk": self.archive.pk})
        response = self.client.get(url)
        #self.assertEqual(response.status.code, 200) #one way, or:
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_html_detail_with_failure(self):
        url = reverse('archive-detail', kwargs={"pk": 123456789})    #url = /archive/123456789/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass