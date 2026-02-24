from sense_hat import SenseHat
import time
sense = SenseHat()

b = (0,0,0) # Black
a = (255,255,255) # arrow color
n = (255,0,0) # Number / dot color

# Array for just the arrow
arrow_pixels = [
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a,
    a, a, a, a, a, a, a, a, 
    a, a, a, a, a, a, a, a, 
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a,
    b, b, b, b, b, b, a, a
]

my_arrow = arrow_pixels.copy()

def idGen(id):
    # Adds dots to the proper locations on the arrow
    # Dots are referred to as their location in accordance to the arrow with the
    # front direction facing up, unlike how it is stored sideways in the array
    my_arrow = arrow_pixels.copy()

    if id == 0: # Id of 0 has no dots added
        return

    if (id % 2 == 1): # Top left dot
        my_arrow[56] = a
        my_arrow[57] = a
        my_arrow[48] = a
        my_arrow[49] = a

    if (id % 2 == 0): # Top right dot
        my_arrow[8] = a
        my_arrow[9] = a
        my_arrow[0] = a
        my_arrow[1] = a

    if (id % 4 == 3) or (id > 4 and id % 2 == 0): # Bottom left dot
        my_arrow[59] = a
        my_arrow[60] = a
        my_arrow[51] = a
        my_arrow[52] = a

    if (id % 4 == 0) or (id > 4 and id % 2 == 1): # Bottom right dot
        my_arrow[11] = a
        my_arrow[12] = a
        my_arrow[3] = a
        my_arrow[4] = a

# Display arrow array on sense hat pixels
for i in range(0,9):
    id = i
    idGen(id)
    sense.set_pixels(my_arrow)
    time.sleep(5)

# Clear pixels
sense.clear()