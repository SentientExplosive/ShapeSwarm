import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

from sense_hat import SenseHat

class Brian(Node):
    def __init__(self):
        super().__init__('Bot Ring Wraith Sub')
        # Initialize state publisher
        self.state_pub = self.create_publisher(String, 'state', 10)

        # Initialize megaMail publisher
        self.megaMail = self.create_publisher(String, 'megaMail', 10)

        # Initialize bot positions subscription
        self.bot_pos_ = self.create_subscription(String, 'bot_pos', self.updated_bot_pos,10)

        # Initialize goal positions subscription
        self.goal_pos_ = self.create_subscription(String, 'goal_pos', self.updated_goal_pos,10)

        # Initialize WITIA (Where I Think I Am) subscription
        self.witia_ = self.create_subscription(String, 'witia', self.check_pos_estimate,10)

        # Initialize my ID subscription
        self.my_id_ = self.create_subscription(String, 'my_id', self.id_updater,10)

        # Initialize Error State subscription
        self.error_state_ = self.create_subscription(Int64, 'errorState', self.error_state_handler,10)

        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)

        # State variable
        self.currState = 0

        # Other Variables
        self.my_pos = []
        self.goals = []

        # Sense hat stuff
        self.sense = SenseHat()

        b = (0,0,0) # Black
        a = (0,0,255) # arrow color
        self.n = (255,0,0) # Number / dot color

        # Array for just the arrow
        self.arrow_pixels = [
            b, b, b, b, b, b, a, a,
            b, b, b, b, b, b, a, a,
            b, b, b, b, b, b, a, a,
            a, a, a, a, a, a, a, a, 
            a, a, a, a, a, a, a, a, 
            b, b, b, b, b, b, a, a,
            b, b, b, b, b, b, a, a,
            b, b, b, b, b, b, a, a
        ]
        self.my_arrow = self.arrow_pixels.copy()

        self.get_logger().info("Done initializing")

    # ROS Node Functions (if any)
    def error_state_handler(self, msg): # To be added
        pass
    
    def state_updater(self, msg):
        # Updates the state of the system
        newState = msg.data
        self.currState = newState

    def id_updater(self, msg):
        self.ID = msg.data
        self.my_arrow = self.idGen(self.ID)
        self.sense.set_pixels(self.my_arrow)
    
    def updated_bot_pos(self, msg):
        pos = eval(msg.data)
        self.other_pos = [pos[i] for i in range(len(pos)) if i != self.ID]
        self.my_pos = pos[self.ID]
        self.updateBotField()
        
    def updated_goal_pos(self, msg):
        self.goals = eval(msg.data)
        self.updateGoalField()

    def check_pos_estimate(self, msg): # Functionality for this is mostly redundant, more to see if the Mega is doing a good job with encoders & PID
        pos = eval(msg)

    # Sense Hat stuff
    def idGen(self, id):
        # Adds dots to the proper locations on the arrow
        # Dots are referred to as their location in accordance to the arrow with the
        # front direction facing up, unlike how it is stored sideways in the array
        my_id = self.arrow_pixels.copy()

        if (id % 2 == 1): # Top left dot
            print("Top Left")
            my_id[56] = self.n
            my_id[57] = self.n
            my_id[48] = self.n
            my_id[49] = self.n

        if (id % 8 > 3): # Top right dot
            print("Top Right")
            my_id[8] = self.n
            my_id[9] = self.n
            my_id[0] = self.n
            my_id[1] = self.n

        if (id % 4 > 1): # Bottom left dot
            print("Bottom Left")
            my_id[59] = self.n
            my_id[60] = self.n
            my_id[51] = self.n
            my_id[52] = self.n

        if (id % 16 > 7): # Bottom right dot
            print("Bottom Right")
            my_id[11] = self.n
            my_id[12] = self.n
            my_id[3] = self.n
            my_id[4] = self.n

        return my_id

    # Potential field calculations
    def updateGoalField(self):
        # Creates the base goal potential field
        pass

    def updateBotField(self):
        # Add bot repulsion factor to the basic field & send [force, my_pos] to Mega
        pass

def main(args=None):
    rclpy.init(args=args)
    node = Brian()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Brian.")
    finally:
        # Clear pixels & destroy node
        node.sense.clear()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()