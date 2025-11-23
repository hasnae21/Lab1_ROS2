#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PongNode(Node):
    """
    Répond par 'PONG #n' lorsqu'un 'PING #n' est reçu.
    """

    def __init__(self):
        super().__init__('pong_node')

        self.subscription = self.create_subscription(
            String,
            'ping_topic',
            self.ping_callback,
            10
        )

        self.publisher_ = self.create_publisher(String, 'pong_topic', 10)

        self.get_logger().info("Pong node started! Listening on /ping_topic")

    def ping_callback(self, msg):
        ping_msg = msg.data  # ex: "PING #3"
        self.get_logger().info(f"Received {ping_msg}, sending PONG")

        pong_msg = String()
        pong_msg.data = ping_msg.replace("PING", "PONG")

        self.publisher_.publish(pong_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PongNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
