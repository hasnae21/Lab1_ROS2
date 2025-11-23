#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class PingNode(Node):
    """
    Envoie des PING, reçoit des PONG, et calcule le round-trip time.
    """

    def __init__(self):
        super().__init__('ping_node')

        # Publisher → /ping_topic
        self.publisher_ = self.create_publisher(String, 'ping_topic', 10)

        # Subscriber → /pong_topic
        self.subscription = self.create_subscription(
            String,
            'pong_topic',
            self.pong_callback,
            10
        )

        # Compteur de ping
        self.ping_count = 0

        # Temps d'envoi (pour RTT)
        self.last_ping_time = None

        # Timer → envoie un ping toutes les 2 secondes
        self.timer = self.create_timer(2.0, self.send_ping)

        self.get_logger().info("Ping node started! Publishing on /ping_topic")

    def send_ping(self):
        self.ping_count += 1

        msg = String()
        msg.data = f"PING #{self.ping_count}"

        self.last_ping_time = time.time()

        self.publisher_.publish(msg)
        self.get_logger().info(f"Sent {msg.data}")

    def pong_callback(self, msg):
        received = msg.data  # ex: "PONG #3"
        now = time.time()

        if self.last_ping_time:
            rtt = (now - self.last_ping_time) * 1000.0  # ms
        else:
            rtt = -1

        self.get_logger().info(
            f"Received {received} | Round-trip time = {rtt:.2f} ms"
        )


def main(args=None):
    rclpy.init(args=args)
    node = PingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
