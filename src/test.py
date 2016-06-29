import src.utils.camera.SbigDriver as SbigDriver
from time import sleep

c = 0
while c < 3:
    print("photo {}".format(c))
    SbigDriver.open_driver()
    SbigDriver.open_deviceusb()
    SbigDriver.establishinglink()

    SbigDriver.photoshoot(1 * 100, "oi", 1)

    SbigDriver.close_device()
    SbigDriver.close_driver()

    c+=1
    sleep(2)