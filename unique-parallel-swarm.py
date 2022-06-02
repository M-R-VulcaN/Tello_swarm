from tello import Tello
from swarm import TelloSwarm
from time import sleep
from threading import Thread


"""
    In this example we use 2 tellos to do something unique in parallel using threads,
    each tello unique action is written in func1, func2.
"""


def initializeSwarm():
    """
    This function initializes the tello swarm by giving the network interfaces to which the
    Tello will be connected. Enters the drones to SDK mode and disables the stream of the drones.
    *Note*: in order to get the interfaces names you should run the command: ifconfig in your terminal.
    Look in Tello-WIKI to understand better!
    """

    swarm = TelloSwarm.fromInterfaces([
        'wlp3s0',
        'wlx386b1ce2083d'
    ])

    swarm.connect() # Enter the drones to SDK mode
    swarm.streamoff()
    return swarm

# Action for example that drone1 should do
def func1(drone: Tello):
    sleep(0.2) # necessary in order to avoid errors
    drone.move_up(40)
    drone.move_down(40)

# Action for example that drone2 should do
def func2(drone: Tello):
    sleep(0.2) # necessary in order to avoid errors
    drone.move_down(30)
    drone.move_up(40)


def main():
    swarm = initializeSwarm()
    swarm.takeoff() # takeoff the drones

    telloDrones = swarm.getTellos() # get all the tellos in the swarm
    sleep(3) # necessary in order to avoid errors
    drone_threads = [Thread(target = func1, args=(telloDrones[0],)),
                    Thread(target = func2, args=(telloDrones[1],))]

    for x in drone_threads:
        x.start() # start the threads 

    for x in drone_threads:
        x.join() # wait until it ends to continue

    swarm.land() # land the drones
    swarm.end() # close the connection


if __name__ == "__main__":
    main()
