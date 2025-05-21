import unittest

from src.utils import keyword_match, salary_threshold, sort_by_pay
from src.vacancy import JobInfo


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.jobs = [
            JobInfo("Python Dev", "Company A", 100000, 150000, "RUB", "link1"),
            JobInfo("Java Dev", "Company B", 80000, 120000, "RUB", "link2"),
            JobInfo("C++ Dev", "Company C", 50000, 100000, "RUB", "link3"),
        ]

    def test_keyword_match(self):
        matched = keyword_match(self.jobs, "Python")
        self.assertEqual(len(matched), 1)

    def test_salary_threshold(self):
        jobs = [
            JobInfo("Dev", "A", 120_000, 150_000, "RUB", "link1"),
            JobInfo("Tester", "B", 100_000, 110_000, "RUB", "link2"),
            JobInfo("Intern", "C", 80_000, 90_000, "RUB", "link3")
        ]
        filtered = salary_threshold(jobs, 100_000)
        self.assertEqual(len(filtered), 2)

    def test_sort_by_pay(self):
        sorted_jobs = sort_by_pay(self.jobs)
        self.assertEqual(sorted_jobs[0].min_pay, 100000)
