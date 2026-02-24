from sense_hat import SenseHat
import time
sense = SenseHat()

b = (0,0,0) # Black
a = (255,255,255) # arrow color
n = (255,0,0) # Number / dot color

# Array for just the arrow
arrow_pixels = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, a, a,
    a, a, a, a, a, a, a, a, 
    a, a, a, a, a, a, a, a, 
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a
]

# Display arrow array on sense hat pixels
sense.set_pixels(arrow_pixels)
time.sleep(5)

# Clear pixels
sense.clear()