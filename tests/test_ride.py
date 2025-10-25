import unittest
from driver import Driver
from rider import Rider
from ride import Ride

RATE_PER_KM = 10

class TestRide(unittest.TestCase):
    def setUp(self):
        self.driver = Driver("John", "Toyota Corolla")
        self.rider = Rider("Alice")

    def test_ride_initialization(self):
        ride = Ride(self.driver, self.rider, 5)
        self.assertEqual(ride.status, "requested")
        self.assertEqual(ride.distance, 5)
        self.assertEqual(ride.driver, self.driver)
        self.assertEqual(ride.rider, self.rider)

    def test_cost_calculation(self):
        ride = Ride(self.driver, self.rider, 5)
        self.assertAlmostEqual(ride.cost, 5 * RATE_PER_KM)

    def test_status_transition(self):
        ride = Ride(self.driver, self.rider, 5)
        ride.start_ride()
        self.assertEqual(ride.status, "in_progress")
        ride.complete_ride()
        self.assertEqual(ride.status, "completed")
