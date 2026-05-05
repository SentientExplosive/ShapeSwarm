import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64
# from std_msgs.msg import Float32
import serial
# import time

class SerialCommunicator(Node):
    def __init__(self):
        super().__init__('megaComms')
        # Initialize WITIA publisher
        self.witia = self.create_publisher(String, 'WITIA', 10)

        # Initialize Error State publisher
        self.errorState = self.create_publisher(Int64, 'errorState', 10)

        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)
        
        # Initialize MegaMail subscription (messages being sent to the mega)
        self.megaMail_ = self.create_subscription(String, 'megaMail', self.send_serial_data, 10)

        # Initialize the serial port
        # Update the serial port name and baud rate as needed (should add code to search for open ports and trying to connect to them, or dedicate a specific port to the PI)
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.port_open= True

        # Initialize timer to call the read_serial_data function every 'timer_period' seconds (0.01)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.read_serial_data)

        # Variable to store current state of the system
        self.currState = 0

        # Preset states of the system
        self.RUNSTATE = 1
        
        self.get_logger().info("Done initializing")

    def read_serial_data(self):
        # Attempt to read data from the serial port
        try:
            if (self.ser.in_waiting > 0 and self.port_open and self.currState == self.RUNSTATE):
                # Read line in from serial port
                line = self.ser.readline().decode('utf-8').strip()
                
                # Split string by ; in case multiple lines merged into one
                data = line.split(";")

                # Iterate through data recieved in the line that was read
                for part in data:
                    if part[0:6] == "WITIA*": # Checks if the beginning of the data segment is the start code S*
                        # String justification & stripping
                        string_data = part[6:]
                        self.get_logger().info(string_data)

                        # Send WITIA data to the topic
                        WITIA = String()
                        WITIA.data = string_data
                        self.witia.publish(WITIA)
        
        # In the case of an error, close the port and output the error
        except serial.SerialException as e:
            # Log the error in console
            self.get_logger().info("Error: %s" % e)

            # Send error to Brian
            eState = Int64()
            eState.data = 1
            self.errorState.publish(eState)

            # Mark the port as closed
            self.port_open = False

    def state_updater(self, msg):
        # Updates the state of the system
        newState = msg.data
        self.currState = newState

    def send_serial_data(self, msg):
        # Sends serial data to the rp2040 based on the data in the msg variable passed to the function
        if (self.currState == self.RUNSTATE):
            message = msg.data
            try:
                self.ser.write(message.encode('utf-8'))
            except:
                self.get_logger().info("Error when trying to send message: %s" % message)
        elif (self.currState != self.RUNSTATESTATE):
            message = eval(msg.data)
            message = repr([0,0,message[2],message[3]])
            try:
                self.ser.write(message.encode('utf-8'))
            except:
                self.get_logger().info("Error when trying to send message: %s" % message)

    def destroy_node(self): # Destroys the node at end of program execution
        self.ser.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = SerialCommunicator()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down serial communications.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()