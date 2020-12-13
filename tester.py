
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def dither_fill(wait, start, end, colorstart, colorend):
    for j in range(start, end):
        pixels[j] = Dither(ComputePower(j-start,end-start), colorstart, colorend)
    pixels.show()
    time.sleep(wait)
    
  
    
    #Fill Red
    #pixels.fill((255, 0, 0))
    #pixels.show()
    #time.sleep(1)


    #Fill Green
    #pixels.fill((0, 255, 0))
    #pixels.show()
    #time.sleep(1)

    #Fill Blue
    #pixels.fill((0, 0, 255))
    #pixels.show()
    #time.sleep(1)


    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    
    # dither_fill(10, 0, 100, BigCRGB(255,0,0), BigCRGB(0,0,255))
