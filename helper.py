def elapsedtime(then, now):
	return (now - then)

# -------------------------------------------------------------------------------------
# Common routines to find pixel color values from 2 seperate pixel colors.

# Compute from Power of pixel with from time start to time end.
def ComputePower(fltElapsed,  FltDuration):
    return (fltElapsed / FltDuration)
  

# Compute from Power of pixel with from time start to time end.
#  For pixels that are split to behave differently on first half of time.
#  Compute First half or Bottom half value.
def ComputePowerHalfBot( fltElapsed,  FltDuration):
    return (fltElapsed * 2 / FltDuration)
  

# Compute from Power of pixel with from time start to time end.
#  For pixels that are split to behave differently on first half of time.
#  Compute Second half or Top half value.
def ComputePowerHalfTop( fltElapsed,  FltDuration):
    return (1 - (((fltElapsed *2 ) - FltDuration) / FltDuration))
  

# Merge two pixel colors based on Power.  Returns the bigCRGB value from CRGB.
def Dither(fltPower, crgbColor1, crgbColor2):
    tmpColor.r = (fltPower * crgbColor2.r) + ((1 - fltPower) * crgbColor1.r)
    tmpColor.g = (fltPower * crgbColor2.g) + ((1 - fltPower) * crgbColor1.g)
    tmpColor.b = (fltPower * crgbColor2.b) + ((1 - fltPower) * crgbColor1.b)
    return tmpColor
    
  
# Common routines to find pixel color values from 2 seperate pixel colors.

# Compute from Power of pixel with from time start to time end.
def ComputePower(fltElapsed, FltDuration):
    return (fltElapsed / FltDuration);

# Compute from Power of pixel with from time start to time end.
#  For pixels that are split to behave differently on first half of time.
#  Compute First half or Bottom half value.
def ComputePowerHalfBot( fltElapsed,  FltDuration):
    return (fltElapsed * 2 / FltDuration)


# Compute from Power of pixel with from time start to time end.
#  For pixels that are split to behave differently on first half of time.
#  Compute Second half or Top half value.
def ComputePowerHalfTop( fltElapsed,  FltDuration):
    return (1 - (((fltElapsed *2 ) - FltDuration) / FltDuration))


#Merge two pixel colors based on Power.  Returns the bigCRGB value from CRGB.
def Dither(fltPower,crgbColor1,crgbColor2):
    tmpColor = BigCRGB(0,0,0)
    tmpColor.r = (fltPower * crgbColor2.r) + ((1 - fltPower) * crgbColor1.r)
    tmpColor.g = (fltPower * crgbColor2.g) + ((1 - fltPower) * crgbColor1.g)
    tmpColor.b = (fltPower * crgbColor2.b) + ((1 - fltPower) * crgbColor1.b)
    return tmpColor.get_color()


# Merge two pixel colors based on Power.  Returns the bigCRGB value from CRGB.
def DitherSmall(fltPower, crgbColor1, crgbColor2):
    
    tmpColor.r = (fltPower * crgbColor2.r) + ((1 - fltPower) * crgbColor1.r)
    tmpColor.g = (fltPower * crgbColor2.g) + ((1 - fltPower) * crgbColor1.g)
    tmpColor.b = (fltPower * crgbColor2.b) + ((1 - fltPower) * crgbColor1.b)
    return tmpColor
