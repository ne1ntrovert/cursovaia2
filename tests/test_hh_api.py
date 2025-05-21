import unittest
from unittest.mock import patch

import requests

from src.hh_api import HHGateway
from src.vacancy import JobInfo


class TestHHGateway(unittest.TestCase):
    @patch("src.hh_api.requests.get")
    def test_ping_success(self, mock_get):
        mock_get.return_value.status_code = 200
        gateway = HHGateway()
        self.assertTrue(gateway.ping())

    @patch("src.hh_api.requests.get")
    def test_ping_fail(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")
        gateway = HHGateway()
        self.assertFalse(gateway.ping())

    @patch("src.hh_api.requests.get")
    def test_fetch_jobs(self, mock_get):
        mock_response = {
            "items": [
                {
                    "name": "Python Dev",
                    "employer": {"name": "Компания"},
                    "salary": {"from": 100000, "to": 150000, "currency": "RUB"},
                    "alternate_url": "https://link"
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        gateway = HHGateway()
        jobs = gateway.fetch("Python", 1)
        self.assertEqual(len(jobs), 1)
        self.assertIsInstance(jobs[0], JobInfo)
 29 changes: 29 additions & 0 deletions29
tests/test_savers.py
Viewed
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,29 @@
import os
import unittest

from src.savers import JSONHandler
from src.vacancy import JobInfo


class TestJSONHandler(unittest.TestCase):
    def setUp(self):
        self.path = "test_data.json"
        self.handler = JSONHandler(path=self.path)
        self.handler.clear()

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_write_and_read(self):
        job = JobInfo("Tester", "QA Ltd", 60000, 80000, "RUB", "test_link")
        self.handler.write([job])
        data = self.handler.read()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].name, "Tester")

    def test_clear(self):
        self.handler.write([JobInfo("Test", "Emp", 1, 2, "RUB", "link")])
        self.handler.clear()
        data = self.handler.read()
        self.assertEqual(data, [])
