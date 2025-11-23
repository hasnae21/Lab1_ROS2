#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class NumberDoubler(Node):
    """
    S'abonne à '/number', double la valeur reçue, log l'info
    et republie le double sur '/number_doubled'.
    """
    def __init__(self):
        super().__init__('number_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'number',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(Int32, 'number_doubled', 10)
        self.get_logger().info('Number subscriber started: listening on /number')

    def listener_callback(self, msg):
        received = msg.data
        doubled = received * 2
        self.get_logger().info(f'Received: {received} -> Doubled: {doubled}')

        out_msg = Int32()
        out_msg.data = doubled
        self.publisher_.publish(out_msg)
        self.get_logger().info(f'Published doubled value on /number_doubled: {doubled}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberDoubler()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
