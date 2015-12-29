import os.path
import unittest
from urlparse import urlparse
import json
from urllib2 import urlopen

from mock import patch


class ClientAPI(object):
    def request(self, lat, long, year):
        url = "http://localhost:8000/api/v1/map_score/?latitude=%s&longitude=%s&year=%s" % (lat, long, year)
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)


class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.client = ClientAPI()

    def test_request(self):
        """Test a simple request."""
        lat = '48.43246421276123'
        long = '-89.37034606933594'
        year = '2013'

        response = self.client.request(lat, long, year)
        results = response['results'][0]
        self.assertIn('grade', results)
        self.assertEqual(results['grade'], 100.0)
        self.assertEqual(results['score'], 1)
