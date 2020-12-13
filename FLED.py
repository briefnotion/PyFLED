# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

from helper import *



class BigCRGB:
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b
        
    def get_color(self):
        return (int(self.r), int(self.g), int(self.b))
        
class animation_properties:
    def __init__(self):
        self.timecreated
        self.animation_duration
        self.animation_speed
        self.pixel_animation
        self.start_pos
        self.end_pos
        self.repeat
        self.clearwhencomplete
        self.animation_pixels[end_pos-start_]
        
class aniation_pixel_properties:
    def __init_(self):
        self.duration
        
class animation_:
    def __init__(self):
        self.speed

    





# How long should our cycles take.
CycleTime = .0250

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)



def RenderAnimations():
    #testAnimation
    #sudoanimation
    elapsedtime = time.time() - step
    if elapsedtime > 10:
        step = time.time()
        elapsedtime = 0
    
    for j in range(0, num_pixels):
        #print (ComputePower(elapsedtime, 10))
        pixels[j] = Dither((ComputePower(elapsedtime, 10)), BigCRGB(255,0,0), BigCRGB(0,0,255))
        UpdateStrip = True


#SETUP
step = time.time()


#MAIN LOOP
while True:
    # Events and Light Path animations should only be called when their time is up.


    # Only update the hardware when changes have been detected.
    #   This vabiable will be checked at the end of the loop.  If nothing was updated,
    #   the loop will just walk on past any hardware updates that would otherwise be
    #   sent.
    UpdateStrip = False


    # Get current time.  This will be our timeframe to work in.
    cyclestarttime = time.time()
    
    # --- Begin of Delayless Loop ---

    
    # --- Grabbing Data From Hardware inputs ---
    # ---

    # Check the doors and start or end all animations
    # *** This will be an event, but letf here as a placeholder.
    # DoorMonitorAndAnimationControlModule(lsStrips, teEvent, hwDoors, booSensors, tmeCurrentMillis);
    
    # --- Check and Execute Timed Events That Are Ready ---

    #  Timed Event ALL GLOBAL, or Scheduled Task
    # *** This will be an event, but letf here as a placeholder.
    #  teSystem(lsStrips, teEvent, tmeCurrentMillis);

    # Update Pixel with Animations
    # UpdateStrip = teEvent[0].execute(sRND, hwLEDs0, tmeCurrentMillis);
    RenderAnimations()
    
    


    # If we made it to this part of the code then we need to
    #   tell the LED hardware that it has a change to commit.

    # --- Execute LED Hardware Changes If Anything Was Updated ---
    if UpdateStrip == True:
        pixels.show()
        
    # Sleep until ready to cycle again.
    sleeptime = CycleTime - (elapsedtime(cyclestarttime, time.time()))
    print(sleeptime)
    if sleeptime > 0:
        time.sleep(sleeptime)
        print(sleeptime)
    

