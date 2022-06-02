from tello import Tello
from swarm import TelloSwarm
from time import sleep


"""
    In This example we use 2 tellos to make each tello do actions in parallel.
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
    swarm.streamoff() #disable the stream of camera
    return swarm



def main():
    swarm = initializeSwarm()
    swarm.takeoff() # takeoff the drones
    
    #move all the drones up 40 cm
    swarm.move_up(40)

    #rotate 360 clockwise all of the drones in the swarm
    swarm.rotate_clockwise(360)

    swarm.land() # land the drones
    swarm.end() # close the connection


if __name__ == "__main__":
    main()
