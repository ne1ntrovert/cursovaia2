import unittest

from src.vacancy import JobInfo


class TestJobInfo(unittest.TestCase):
    def setUp(self):
        self.job = JobInfo("Python Dev", "ООО Рога", 100000, 150000, "RUB", "https://example.com")

    def test_repr(self):
        self.assertIn("Python Dev", repr(self.job))

    def test_serialize(self):
        data = self.job.serialize()
        self.assertEqual(data["position"], "Python Dev")
        self.assertEqual(data["min_salary"], 100000)

    def test_comparison(self):
        other = JobInfo("Java Dev", "ООО Копыта", 90000, 120000, "RUB", "link")
        self.assertTrue(self.job > other)

    def test_sanitize_negative_salary(self):
        job = JobInfo("Fake", "BadCo", -100, None, "USD", "link")
        self.assertEqual(job.min_pay, 0)
