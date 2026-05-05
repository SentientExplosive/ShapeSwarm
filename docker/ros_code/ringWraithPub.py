# python 3.11
# Non-ROS Code taken from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import paho.mqtt.client as mqtt_client

class ringWraithPub(Node):
    def __init__(self):
        super().__init__('Bot_Ring_Wraith_Pub')
        # Initialize Error State publisher
        self.errorState = self.create_publisher(Int64, 'errorState', 10)

        # Initialize goal_reached subscription
        self.goal_reached_ = self.create_subscription(Int64, 'goal_reached', self.send_goal_reached, 10)

        # Initialize my_ID subscription
        self.my_id = self.create_subscription(Int64, 'my_id', self.id_updater,10)

        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)

        # State variable
        self.currState = 0

        # MQTT Variables
        self.broker = "137.142.164.255"
        self.port = 1883
        self.botID = 0 # This will update automatically as the bots fight over IDs
        self.topicPrefix = 'toSauron'
        self.GOAL_TOPIC = '/goal_reached'
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
    
    def id_updater(self, msg):
        self.botID = msg.data

    def send_goal_reached(self, msg):
        val = msg.data
        if val == 1: # Goal reached!
            msg = 1
            self.run(1)

    # MQTT Functions
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.get_logger().info("Connected to MQTT Broker!")
            else:
                self.get_logger().info(f"Failed to connect, return code {rc}\n")
        
        # Removing disconnect method here to avoid conflicts with the subscriber setting a new bot ID on conflict
        # def on_disconnect(client, userdata, rc):
            # self.botID += 1
            # self.get_logger().info(f"Bot ID: {self.botID}")

        # Generate a Client ID with the subscribe prefix.
        client_id = f'publish-bot{self.botID}'

        # Start client
        # client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2,client_id)
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        # client.on_disconnect = on_disconnect
        client.username_pw_set(self.username, self.password)
        client.connect(self.broker, self.port, 60)
        return client

    def publish(self, client, msg):
        topic = self.topicPrefix + self.GOAL_TOPIC
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            self.get_logger().info(f"Send `{msg}` to topic `{topic}`")
        else:
            self.get_logger().info(f"Failed to send message to topic {topic}")

    def run(self, msg=0):
        client = self.connect_mqtt()
        client.loop_start()
        self.publish(client, msg)
        client.loop_stop()


def main(args=None):
    rclpy.init(args=args)
    node = ringWraithPub()
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