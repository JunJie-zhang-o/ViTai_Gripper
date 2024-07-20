import time


# from Robotiq.HandE import HandEForRtu
from Robotiq import HandEForRtu

# ! you need to change the port.
# * In linux, you can ls /dev/ttyUSB* to found the usb port
# * In Mac,  you can ls /dev/tty* to found the usb port
# * In Win, you can find the com port.

port = "/dev/tty.usbserial-AQ00O97B"
hande = HandEForRtu(port=port)
time.sleep(1)
while True:
    hande.move(0,0,0,True)
    hande.move(50,1,3,False)
    # time.sleep(1)
    hande.stop()
    time.sleep(1)
    hande.move(50,1,3,True)