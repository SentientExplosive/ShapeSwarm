# python 3.11
# Non-ROS Code taken from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import paho.mqtt.client as mqtt_client

class ringWraithSub(Node):
    def __init__(self):
        super().__init__('Bot_Ring_Wraith_Sub')
        # Initialize bot positions publisher
        self.bot_pos = self.create_publisher(String, 'bot_pos', 10)

        # Initialize goal positions publisher
        self.goal_pos = self.create_publisher(String, 'goal_pos', 10)

        # Initialize my ID publisher (not sure if this will be needed)
        self.my_id = self.create_publisher(String, 'my_id', 10)

        # Initialize Error State publisher
        self.errorState = self.create_publisher(Int64, 'errorState', 10)

        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)

        # State variable
        self.currState = 0

        # MQTT Variables
        self.broker = "137.142.164.255"
        self.port = 1883
        self.botID = 0 # This will update automatically as the bots fight over IDs
        self.subscriptionTopic = [('fromSauron/#',0)]
        self.username = 'Sauron'
        self.password = 'rOb0t1cs#'
        

        # Start MQTT service
        self.run()

        self.get_logger().info("Done initializing")

    # ROS Node Functions (if any)
    def state_updater(self, msg):
        # Updates the state of the system
        newState = msg.data
        self.currState = newState

    # MQTT Functions
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.get_logger().info("Connected to MQTT Broker!")
            else:
                self.get_logger().info(f"Failed to connect, return code {rc}\n")
        
        def on_disconnect(client, userdata, rc):
            self.botID += 1
            myID = Int64()
            myID.data = self.botID
            self.my_id.publish(myID)
            self.get_logger().info(self.botID)

        # Generate a Client ID with the subscribe prefix.
        client_id = f'subscribe-bot{self.botID}'

        # Start client
        # client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2,client_id)
        client = mqtt_client.Client(client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.username_pw_set(self.username, self.password)
        client.connect(self.broker, self.port, 60)
        return client
    
    def send_bot_pos(self, msg):
        pos = String()
        pos.data = msg
        self.bot_pos.publish(pos)
    
    def send_goal_pos(self, msg):
        gPos = String()
        gPos.data = msg
        self.goal_pos.publish(gPos)
    
    def send_my_ID(self, msg):
        myID = Int64()
        myID.data = msg
        self.my_id.publish(myID)

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            self.get_logger().info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            if msg.topic == "fromSauron/bot_pos":
                self.send_bot_pos(msg.payload.decode())
            elif msg.topic == "fromSauron/goal_pos":
                self.send_goal_pos(msg.payload.decode())
            elif msg.topic == "":
                self.send_my_ID(msg.payload.decode())


        client.subscribe(self.subscriptionTopic)
        client.on_message = on_message

    def run(self):
        client = self.connect_mqtt()
        self.subscribe(client)
        client.loop_start()


def main(args=None):
    rclpy.init(args=args)
    node = ringWraithSub()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Pi to Eye comms subscriber.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()