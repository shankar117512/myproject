from django.test import TestCase


class MyTest(TestCase):  # class name can be anything
    def test_sample(self):  # MUST start with test_
        self.assertEqual(1, 1)
