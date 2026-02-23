import time
import random


class Drone:

    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.battery = 100
        self.status = "Idle"
        self.location = "Hospital Base"

    def takeoff(self):
        self.status = "Taking Off"
        print(f"{self.drone_id} taking off...")
        time.sleep(1)

    def fly_to_location(self, location):
        self.status = "Flying"
        print(f"{self.drone_id} flying to {location}...")
        time.sleep(2)
        self.location = location
        self.battery -= random.randint(10, 20)

    def deliver_package(self):
        self.status = "Delivering"
        print(f"{self.drone_id} delivering medical package...")
        time.sleep(1)

    def return_home(self):
        self.status = "Returning"
        print(f"{self.drone_id} returning to base...")
        time.sleep(2)
        self.location = "Hospital Base"

    def land(self):
        self.status = "Landed"
        print(f"{self.drone_id} landed successfully.")