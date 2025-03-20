# Write your code here :-)


from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(4),16)

np[0] = (240,0,0)
np[12] = (0,226,255)
np[10] = (218,255,173)
np.write()
print("69420")
