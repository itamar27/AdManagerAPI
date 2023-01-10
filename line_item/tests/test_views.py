from django.utils import timezone
from rest_framework.test import APITestCase

from line_item.models import LineItem
from ad_unit.models import AdUnit


class TestAdUnitAPI(APITestCase):

    def setUp(self):
        self.url = '/api/v1/line_item/'

        self.line_item = LineItem.objects.create(
            max_impressions=1000,
            rpm=20.5,
            start_time=timezone.now(),
            end_time=timezone.now()
        )

        self.ad_unit = AdUnit.objects.create(
            country="Israel",
            language="English",
            device="PC",
            os="Windows",
            browser="Chrome"
        )

    def test_get_line_item_with_id(self):
        url = self.url + str(self.line_item.id)
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 200)

    def test_post_new_line_item(self):
        data = {
            "max_impressions": 1001,
            "rpm": 20.5,
            "start_time": timezone.now(),
            "end_time": timezone.now()
        }
        request = self.client.post(self.url, data=data)

        self.assertEqual(request.status_code, 201)

    def test_patch_line_item_with_id(self):
        data = {
            "max_impressions": 1001,
        }
        url = "{0}{1}/".format(self.url, str(self.line_item.id))
        self.client.patch(path=url, data=data)
        request = self.client.get(path=url, follow=True)

        self.assertEqual(request.data['max_impressions'], data['max_impressions'])

    def test_put_line_item_with_id(self):
        data = {
            "max_impressions": 1000,
            "rpm": 10.5,
            "start_time": self.line_item.start_time,
            "end_time": self.line_item.end_time
        }
        url = "{0}{1}/".format(self.url, str(self.line_item.id))
        self.client.put(path=url, data=data)
        request = self.client.get(path=url, follow=True)

        self.assertEqual(request.data['max_impressions'], self.line_item.max_impressions)
        self.assertEqual(request.data['rpm'], data['rpm'])


    def test_delete_line_item_with_id(self):

        url = "{0}{1}/".format(self.url, str(self.line_item.id))
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 200)
        self.client.delete(path=url)
        request = self.client.get(path=url, follow=True)
        self.assertEqual(request.status_code, 404)

    def test_adding_ad_unit_to_line_item(self):

        url = "{0}{1}/".format(self.url, str(self.line_item.id))
        self.client.patch(path=url, data={"targeting": [str(self.ad_unit.id)]})
        request = self.client.get(path=url, follow=True)

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data['targeting'][0], self.ad_unit.id)

    def test_if_deleting_line_item_not_affecting_ad_unit(self):

        url = "{0}{1}/".format(self.url, str(self.line_item.id))
        ad_init_url = "{0}{1}/".format('/api/v1/ad_unit/', str(self.ad_unit.id))

        self.client.patch(path=url, data={"targeting": [str(self.ad_unit.id)]})
        self.client.delete(path=url)

        request = self.client.get(path=ad_init_url, follow=True)

        self.assertEqual(request.status_code, 200)



