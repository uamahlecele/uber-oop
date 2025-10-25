import unittest
from rider import Rider

class TestRider(unittest.TestCase):
    def test_rider_initialization(self):
        r = Rider("Alice")
        self.assertEqual(r.name, "Alice")
        self.assertEqual(r.ride_history, [])

    def test_rider_str(self):
        r = Rider("Alice")
        self.assertIn("Alice", str(r))
