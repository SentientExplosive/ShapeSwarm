from sense_hat import SenseHat
import time
sense = SenseHat()

'''
red = (255,0,0)
blue = (0,0,255)
sense.show_message("Hello World", text_colour=red, back_colour=blue)

r = 0
g = 0
b = 0

for k in range(0,255):
    r = k
    g = k
    b = k

time.sleep(2)

sense.clear((0,0,0)) # sense.clear displays the given color on the screen (in this case black)
'''

time.sleep(3)
# Setting one pixel at a time
sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))
time.sleep(2)

sense.flip_h()
time.sleep(1)
sense.flip_v()
time.sleep(1)


time.sleep(3)
# Setting multiple pixels at the same time
# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)
time.sleep(3)

# Read from the sensors & display values
for i in range(10):

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "T: " + str(t) + " P: " + str(p) + " H: " + str(h)
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05)

time.sleep(3)

# IMU Values
for i in range(10):
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("x={0}, y={1}, z={2}".format(x, y, z))
    time.sleep(0.5)

# Joystick testing
sense.clear()
counter = 0
while counter < 5:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        sense.show_letter("U")      # Up arrow
      elif event.direction == "down":
        sense.show_letter("D")      # Down arrow
      elif event.direction == "left": 
        sense.show_letter("L")      # Left arrow
      elif event.direction == "right":
        sense.show_letter("R")      # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M")      # Enter key
        counter += 1
      
      # Wait a while and then clear the screen
      time.sleep(0.5)
      sense.clear()