#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    """
    A simple subscriber node that listens to messages
    and counts how many messages were received.
    """

    def __init__(self):
        # Initialize the node
        super().__init__('simple_subscriber')

        # Counter for received messages
        self.counter = 0

        # Create subscriber
        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.listener_callback,
            10
        )

        self.get_logger().info('Subscriber node started! Waiting for messages...')

    def listener_callback(self, msg):
        # Increment counter
        self.counter += 1

        # Print message and count
        self.get_logger().info(
            f'I heard: "{msg.data}" | Total messages received: {self.counter}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = SimpleSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
