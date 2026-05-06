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
        self.running = True
        self.count = 0

        # Camera capture
        self.cap = cv2.VideoCapture("/dev/video0")
        if not self.cap.isOpened():
            print("Camera failed to open")
        # Set resolution (optional, like -r 1280x720)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.get_logger().info("Done initializing")

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.sauron)
    
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
        if not self.running:
            return
        
        self.get_logger().info("Opening Eye")
        ret, frame = self.cap.read()
        if not ret:
            self.count += 1
            self.get_logger().info(f'Could not open eye: {self.count}')
            if self.count > 100:
                self.running = False
            return
        self.get_logger().info('Publishing video frame')

        cv2.imshow("LIVE", frame)
        cv2.waitKey(1)


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
        node.cap.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()