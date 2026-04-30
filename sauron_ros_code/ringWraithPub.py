# python 3.11
# Code taken from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

import paho.mqtt.client as mqtt_client

class ringWraithPub(Node):
    def __init__(self):
        super().__init__('Sauron Ring Wraith Pub')
        # Initialize bot positions subscription
        self.bot_pos_ = self.create_subscription(String, 'bot_pos', self.send_bots, 10)

        # Initialize goal positions subscription
        self.goal_pos_ = self.create_subscription(String, 'goal_pos', self.send_goals, 10)

        # Initialize run_state subscription (for updating the current state of the system)
        self.state_ = self.create_subscription(Int64, 'state', self.state_updater,10)

        # State variable
        self.currState = 0

        # MQTT Variables
        self.broker = "137.142.164.255"
        self.port = 1883
        # Generate a Client ID with the publish prefix.
        self.client_id = f'publish-sauron'
        # self.username = 'Sauron'
        # self.password = 'rOb0t1cs#'

        # Topics
        self.topicPrefix = "fromSauron"
        self.GOAL_TOPIC = "/goals"
        self.BOT_TOPIC = "/bots"
        
        # Start MQTT service
        self.run()

        self.get_logger().info("Done initializing")

    # ROS Node Functions (if any)
    def state_updater(self, msg):
        # Updates the state of the system
        newState = msg.data
        self.currState = newState

    def send_bots(self, msg):
        # Sends the bot positions to the bots
        pos = msg.data
        self.run((pos,self.BOT_TOPIC))
    
    def send_goals(self, msg):
        # Sends the goal positions to the bots
        gPos = msg.data
        self.run((gPos,self.GOAL_TOPIC))

    # MQTT Functions
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc, properties):
            if rc == 0:
                ringWraithPub.get_logger().info("Connected to MQTT Broker!")
            else:
                ringWraithPub.get_logger().info("Failed to connect, return code %d\n", rc)
        
        def on_disconnect(client, userdata, flags, rc, properties):
            ringWraithPub.botID += 1
            ringWraithPub.get_logger().info(ringWraithPub.botID)

        # Generate a Client ID with the subscribe prefix.
        client_id = f'subscribe-bot{self.botID}'

        # Start client
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2,client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.connect(self.broker, self.port, 60)
        return client

    def publish(self, client, pub):
        topic = self.topicPrefix + pub[1]
        msg = pub[0]

        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            self.get_logger().info(f"Send `{msg}` to topic `{topic}`")
        else:
            self.get_logger().info(f"Failed to send message to topic {topic}")

    def run(self, pub):
        client = self.connect_mqtt()
        client.loop_start()
        self.publish(client, pub)
        client.loop_stop()


def main(args=None):
    rclpy.init(args=args)
    node = ringWraithPub()
    node.get_logger().info("starting")
    try:
        node.get_logger().info("spinnnnnnn")
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Eye to Pi comms publisher.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()