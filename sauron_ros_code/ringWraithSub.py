# python 3.11
# Non-ROS Code taken from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import paho.mqtt.client as mqtt_client

class ringWraithSub(Node):
    def __init__(self):
        super().__init__('Sauron Ring Wraith Sub')
        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)

        # State variable
        self.currState = 0

        # MQTT Variables
        self.broker = "137.142.164.255"
        self.port = 1883
        self.subscriptionTopic = [('toSauron/#',0)]
        # Generate a Client ID with the subscribe prefix.
        self.client_id = f'subscribe-sauron'
        # self.username = 'Sauron'
        # self.password = 'rOb0t1cs#'

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
        def on_connect(client, userdata, flags, rc, properties):
            if rc == 0:
                ringWraithSub.get_logger().info("Connected to MQTT Broker!")
            else:
                ringWraithSub.get_logger().info("Failed to connect, return code %d\n", rc)

        # Generate a Client ID with the subscribe prefix.
        client_id = f'subscribe-bot{self.botID}'

        # Start client
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2,client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port, 60)
        return client

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            ringWraithSub.get_logger().info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        client.subscribe(self.subscriptionTopic)
        client.on_message = on_message

    def run(self):
        client = self.connect_mqtt()
        self.subscribe(client)
        client.loop_forever()


def main(args=None):
    rclpy.init(args=args)
    node = ringWraithSub()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Eye to Pi comms subscriber.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()