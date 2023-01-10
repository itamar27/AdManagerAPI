from django.db import IntegrityError
from rest_framework.test import APITestCase

from ad_unit.models import AdUnit


class TestAdUnitAPI(APITestCase):

    def setUp(self):
        self.url = '/api/v1/ad_unit/'

        self.ad_unit = AdUnit.objects.create(
            country="Israel",
            language="English",
            device="PC",
            os="Windows",
            browser="Chrome"
        )

    def test_get_ad_unit_with_id(self):
        url = self.url + str(self.ad_unit.id)
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 200)

    def test_post_new_ad_unit(self):
        data = {
            "country": "US",
            "language": "English",
            "device": "Mobile",
            "os": "Windows",
            "browser": "Chrome"
        }
        request = self.client.post(self.url, data=data)

        self.assertEqual(request.status_code, 201)

    def test_patch_ad_unit_with_id(self):
        data = {
            "country": "US",
        }
        url = "{0}{1}/".format(self.url, str(self.ad_unit.id))
        self.client.patch(path=url, data=data)
        request = self.client.get(path=url, follow=True)

        self.assertEqual(request.data['country'], data['country'])

    def test_put_ad_unit_with_id(self):
        data = {
            "country": "US",
            "language": "Arabic",
            "device": "PC",
            "os": "Windows",
            "browser": "Chrome"
        }
        url = "{0}{1}/".format(self.url, str(self.ad_unit.id))
        self.client.put(path=url, data=data)
        request = self.client.get(path=url, follow=True)

        self.assertEqual(request.data['country'], data['country'])
        self.assertEqual(request.data['language'], data['language'])
        self.assertEqual(request.data['device'], data['device'])
        self.assertEqual(request.data['os'], self.ad_unit.os)
        self.assertEqual(request.data['browser'], self.ad_unit.browser)

    def test_delete_ad_unit_with_id(self):
        url = "{0}{1}/".format(self.url, str(self.ad_unit.id))
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 200)
        self.client.delete(path=url)
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 404)
