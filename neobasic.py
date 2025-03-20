# Write your code here :-)


from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(4),16)

np[0] = (255,45,45)
np[12] = (45,45,255)
np[10] = (45,255,45)
np.write()


