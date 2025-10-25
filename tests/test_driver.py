import unittest
from driver import Driver

class TestDriver(unittest.TestCase):
    def test_driver_initialization(self):
        d = Driver("John", "Toyota Corolla")
        self.assertEqual(d.name, "John")
        self.assertEqual(d.car_model, "Toyota Corolla")
        self.assertTrue(d.available)
        self.assertEqual(d.completed_rides, [])

    def test_driver_str(self):
        d = Driver("John", "Toyota Corolla")
        s = str(d)
        self.assertIn("John", s)
        self.assertIn("Toyota", s)

