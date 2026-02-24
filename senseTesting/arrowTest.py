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

def originalIdGen(id):
    # Adds dots to the proper locations on the arrow
    # Dots are referred to as their location in accordance to the arrow with the
    # front direction facing up, unlike how it is stored sideways in the array
    my_id = arrow_pixels.copy()

    if id == 0: # Id of 0 has no dots added
        return my_id

    if (id % 2 == 1): # Top left dot
        print("Top Left")
        my_id[56] = n
        my_id[57] = n
        my_id[48] = n
        my_id[49] = n

    if (id % 2 == 0): # Top right dot
        print("Top Right")
        my_id[8] = n
        my_id[9] = n
        my_id[0] = n
        my_id[1] = n

    if (id % 4 == 3) or (id > 4 and id % 2 == 0): # Bottom left dot
        print("Bottom Left")
        my_id[59] = n
        my_id[60] = n
        my_id[51] = n
        my_id[52] = n

    if (id % 4 == 0) or (id > 4 and id % 2 == 1): # Bottom right dot
        print("Bottom Right")
        my_id[11] = n
        my_id[12] = n
        my_id[3] = n
        my_id[4] = n
    
    print(my_id)
    return my_id

def idGen(id):
    # Adds dots to the proper locations on the arrow
    # Dots are referred to as their location in accordance to the arrow with the
    # front direction facing up, unlike how it is stored sideways in the array
    my_id = arrow_pixels.copy()

    if (id % 2 == 1): # Top left dot
        print("Top Left")
        my_id[56] = n
        my_id[57] = n
        my_id[48] = n
        my_id[49] = n

    if (id % 4 > 1): # Top right dot
        print("Top Right")
        my_id[8] = n
        my_id[9] = n
        my_id[0] = n
        my_id[1] = n

    if (id % 8 > 3): # Bottom left dot
        print("Bottom Left")
        my_id[59] = n
        my_id[60] = n
        my_id[51] = n
        my_id[52] = n

    if (id % 16 > 7): # Bottom right dot
        print("Bottom Right")
        my_id[11] = n
        my_id[12] = n
        my_id[3] = n
        my_id[4] = n
    
    print(my_id)
    return my_id

# Display arrow array on sense hat pixels
for i in range(0,9):
    id = i
    print(id)
    my_arrow = idGen(id)
    print("My arrow")
    print(my_arrow)
    sense.set_pixels(my_arrow)
    time.sleep(5)

# Clear pixels
sense.clear()