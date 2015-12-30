import os.path
import unittest
from home.template.baseimports import urlparse
import json
from urllib2 import urlopen

from mock import patch


class ClientAPI(object):
    def request(self, lat, long, year):
        url = "http://localhost:8000/api/v1/map_score/?latitude=%s&longitude=%s&year=%s" % (lat, long, year)
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)


class ClientTestCaseGood(unittest.TestCase):
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

class ClientTestCaseModerate(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.client = ClientAPI()

    def test_request(self):
        """Test a simple request."""
        lat = '39.58702374799314'
        long = '-105.64092636108398'
        year = '2013'

        response = self.client.request(lat, long, year)
        results = response['results'][0]
        self.assertIn('grade', results)
        self.assertEqual(results['grade'], 85.71428571428571)
        self.assertEqual(results['score'], 2)

class ClientTestCaseUnhealthyForSensitiveGroups(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.client = ClientAPI()

    def test_request(self):
        """Test a simple request."""
        lat = '19.203853465539037'
        long = '-155.48023223876953'
        year = '2013'

        response = self.client.request(lat, long, year)
        results = response['results'][0]
        self.assertIn('grade', results)
        self.assertEqual(results['grade'], 71.42857142857143)
        self.assertEqual(results['score'], 3)

class ClientTestCaseVeryHazardous(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.client = ClientAPI()

    def test_request(self):
        """Test a simple request."""
        lat = '32.49831211917791'
        long = '-116.9765853881836'
        year = '2013'

        response = self.client.request(lat, long, year)
        results = response['results'][0]
        self.assertIn('grade', results)
        self.assertEqual(results['grade'], 14.285714285714285)
        self.assertEqual(results['score'], 7)