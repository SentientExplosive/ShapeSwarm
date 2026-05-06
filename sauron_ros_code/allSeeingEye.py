import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import random
import cv2

class allSeeingEye(Node):
    def __init__(self):
        super().__init__('Sauron')
        # Initialize bot positions publisher
        self.bot_pos = self.create_publisher(String, 'bot_pos', 10)

        # Initialize goal positions publisher
        self.goal_pos = self.create_publisher(String, 'goal_pos', 10)

        # Initialize goal_reached subscription
        self.goal_reached_ = self.create_subscription(Int64, 'goal_reached', self.receive_goal_reached, 10)

        # Whether or not the vision is running (may or may not need this)
        self.running = False

        # Camera capture
        self.cap = cv2.VideoCapture(0)

        self.get_logger().info("Done initializing")

        self.sauron()
    
    def send_bot_pos(self, msg):
        pos = String()
        pos.data = msg
        self.bot_pos.publish(pos)
    
    def send_goal_pos(self, msg):
        gPos = String()
        gPos.data = msg
        self.goal_pos.publish(gPos)
    
    def receive_goal_reached(self, msg):
        pass

    def sauron(self):
        # THE ALL SEEING EYE SEES ALL (hopefully)

        self.get_logger().info("Opening Eye")

        self.running = True
        while self.running:
            ref, frame = self.cap.read()
            if not ref: # if no capture detected, close the program
                self.get_logger().info("Closing Eye")
                self.running = False
                break

            cv2.imshow("LIVE", frame)



def main(args=None):
    rclpy.init(args=args)
    node = allSeeingEye()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Sauron's vision.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()