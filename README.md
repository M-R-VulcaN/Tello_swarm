# Tello_swarm
Tello Non-EDU swarm using wifi adapters.
DJI Tello drone python interface using the official [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf). This library was modified in order to do the swarm using Tello (Non-EDU).
The swarm achived by using multiple wifi adapters in order to connect to each Drone`s network.

## Requirements
- linux (tested on Ubuntu 20.04)
- several wifi-adapters
- python >= 3.6 (tested on 3.8.10)
- opencv (pip install opencv-python)
- netifaces (pip install netifaces)

## Recommended wifi adapters
- DLINK AC1200 [Driver for Ubuntu 20.04](https://askubuntu.com/questions/1312297/usb-wifi-adapter-is-not-working-on-ubuntu-20-04-1-lts)
- DLINK AC600 [Driver for Ubuntu 20.04](https://askubuntu.com/questions/1162974/wireless-usb-adapter-0bdac811-realtek-semiconductor-corp)

## Usage
-import tello
-import swarm
  
