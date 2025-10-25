import unittest
from driver import Driver
from rider import Rider
from ride import Ride
from uber import Uber

class TestUberBonus(unittest.TestCase):
    def setUp(self):
        self.app = Uber()
        self.driver1 = Driver("John", "Toyota Corolla")
        self.driver2 = Driver("Jane", "Honda Fit")
        self.app.add_driver(self.driver1)
        self.app.add_driver(self.driver2)
        self.rider = Rider("Alice")

    def test_cannot_start_completed_ride(self):
        ride = self.app.request_ride(self.rider, distance=10)
        ride.start_ride()
        ride.complete_ride()
        with self.assertRaises(ValueError):
            ride.start_ride()

    def test_request_ride_with_no_drivers(self):
        app = Uber()
        rider = Rider("Alice")
        with self.assertRaises(RuntimeError):
            app.request_ride(rider, distance=5)

    def test_ride_added_to_history(self):
        ride = self.app.request_ride(self.rider, distance=12)
        ride.start_ride()
        ride.complete_ride()
        self.app.mark_ride_completed(ride)
        self.assertIn(ride, self.rider.ride_history)
        self.assertIn(ride, self.driver1.completed_rides)

    def test_invalid_rating_rejected(self):
        ride = self.app.request_ride(self.rider, distance=8)
        ride.start_ride()
        ride.complete_ride()
        with self.assertRaises(ValueError):
            self.rider.rate_driver(ride.driver, 6)

    def test_driver_becomes_unavailable_after_assignment(self):
        ride1 = self.app.request_ride(self.rider, distance=5)
        self.assertFalse(ride1.driver.available)
        # next ride should use a different driver
        ride2 = self.app.request_ride(self.rider, distance=3)
        self.assertNotEqual(ride1.driver, ride2.driver)
