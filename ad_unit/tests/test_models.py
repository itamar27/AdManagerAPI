from django.db import IntegrityError
from django.test import TestCase

from ad_unit.models import AdUnit


class AdUnittest(TestCase):

    def setUp(self):
        AdUnit.objects.create(
            country="Israel",
            language="English",
            device="PC",
            os="Windows",
            browser="Chrome"
        )

    def test_create_new_ad_unit_with_one_different_column(self):
        payload = {
            "country": "US",
            "language": "English",
            "device": "PC",
            "os": "Windows",
            "browser": "Chrome"
        }

        res = AdUnit.objects.create(**payload)

        self.assertEqual(res.country, payload['country'])

    def test_failed_create_same_ad_unit(self):

        with self.assertRaises(IntegrityError):
            AdUnit.objects.create(
                country="Israel",
                language="English",
                device="PC",
                os="Windows",
                browser="Chrome"
            )

