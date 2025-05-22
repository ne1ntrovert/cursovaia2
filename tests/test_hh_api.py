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