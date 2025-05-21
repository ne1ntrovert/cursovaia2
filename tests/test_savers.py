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
