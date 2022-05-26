from tello import Tello
from swarm import TelloSwarm
import cv2
import numpy as np

IMG_RES = (720,960)


"""
    In this example we use 2 tellos to get their video stream and display it.
    You can also do this by typing: ffmpeg -i udp://192.168.10.1:11111?localaddr=192.168.10.2 -f sdl "Tello"
    in the terminal. Note that localaddr is your local adress under the specific interface.
"""

def initializeSwarm():
    """
    This function initializes the tello swarm by giving the network interfaces to which the
    Tello will be connected. Enters the drones to SDK mode and re-enable the stream of the drones.
    *Note*: in order to get the interfaces names you should run the command: ifconfig in your terminal.
    Look in Tello-WIKI to understand better!
    """

    swarm = TelloSwarm.fromInterfaces([
        'wlp3s0',
        'wlxbc0f9a7bfc87',
    ])

    swarm.connect() # Enter the drones to SDK mode
    swarm.streamoff()
    swarm.streamon()
    return swarm


def showDronesStream(telloDrones):
    """
        This function recieves the frames from each Tello
        and displays the frames in one window 
    """
    frame1 = telloDrones[0].get_frame_read() #get frame of drone1
    frame2 = telloDrones[1].get_frame_read() #get frame of drone2

    while True:
        img1 = frame1.frame
        img2 = frame2.frame
        img1 = cv2.resize(img1, IMG_RES)
        img2 = cv2.resize(img2, IMG_RES)
        horizontal_window = np.hstack((img1, img2)) # window with 2 images
        cv2.imshow("Image of drones", horizontal_window)
        if cv2.waitKey(1) & 0xFF == ord('q'): #if 'q' was pressed in the window
            break




def main():
    swarm = initializeSwarm()
    telloDrones = swarm.getTellos() # get all the tellos in the swarm
    showDronesStream(telloDrones)
    swarm.end() # close the connection

if __name__ == "__main__":
    main()
