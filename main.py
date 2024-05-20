import time


# from Robotiq.HandE import HandEForRtu
from Robotiq import HandEForRtu

port = "/dev/tty.usbserial-2120"
hande = HandEForRtu(port=port)
time.sleep(1)
while True:
    hande.move(0,0,0,True)
    hande.move(50,1,3,False)
    # time.sleep(1)
    hande.stop()
    time.sleep(1)
    hande.move(50,1,3,True)