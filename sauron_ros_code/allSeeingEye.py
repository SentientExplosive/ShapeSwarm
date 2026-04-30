import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import random
import cv2

class allSeeingEye(Node):
    def __init__(self):
        super().__init__('megaComms')
        # Initialize bot positions publisher
        self.bot_pos = self.create_publisher(String, 'bot_pos', 10)

        # Initialize goal positions publisher
        self.goal_pos = self.create_publisher(String, 'goal_pos', 10)

        # Initialize goal_reached subscription
        self.goal_reached_ = self.create_subscription(Int64, 'goal_reached', self.receive_goal_reached, 10)

        self.running = False

        self.get_logger().info("Done initializing")
    
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



def main(args=None):
    rclpy.init(args=args)
    node = allSeeingEye()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Pi to Eye comms publisher.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()