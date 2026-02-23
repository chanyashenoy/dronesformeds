from backend.drone import Drone

def run_delivery_mission():

    drone = Drone("MEDI-01")

    destination = "Village A"

    print("\nMission Started\n")

    drone.takeoff()
    drone.fly_to_location(destination)
    drone.deliver_package()
    drone.return_home()
    drone.land()

    print("\nMission Completed\n")


if __name__ == "__main__":
    run_delivery_mission()