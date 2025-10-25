import unittest
from driver import Driver
from rider import Rider
from uber import Uber

class TestUber(unittest.TestCase):
    def setUp(self):
        self.app = Uber()
        self.driver1 = Driver("John", "Toyota Corolla")
        self.driver2 = Driver("Jane", "Honda Fit")
        self.app.add_driver(self.driver1)
        self.app.add_driver(self.driver2)
        self.rider = Rider("Alice")

    def test_add_driver(self):
        self.assertIn(self.driver1, self.app.available_drivers)
        self.assertTrue(self.driver1.available)

    def test_request_ride_assigns_driver(self):
        ride = self.app.request_ride(self.rider, distance=8)
        self.assertEqual(ride.driver.available, False)
        self.assertIn(ride, self.app.active_rides)

    def test_completed_ride_makes_driver_available(self):
        ride = self.app.request_ride(self.rider, distance=8)
        ride.start_ride()
        ride.complete_ride()
        self.app.mark_ride_completed(ride)
        self.assertTrue(ride.driver.available)
        self.assertIn(ride, self.app.completed_rides)
        self.assertNotIn(ride, self.app.active_rides)

    def test_rider_can_rate_driver(self):
        ride = self.app.request_ride(self.rider, distance=10)
        ride.start_ride()
        ride.complete_ride()
        self.app.mark_ride_completed(ride)

        self.rider.rate_driver(ride.driver, 5)
        self.assertEqual(ride.driver.average_rating, 5.0)

        # multiple ratings
        self.rider.rate_driver(ride.driver, 4)
        self.assertAlmostEqual(ride.driver.average_rating, 4.5)
