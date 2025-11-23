#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class NumberPublisher(Node):
    """
    Publie des entiers sur le topic '/number' toutes les secondes.
    """
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'number', 10)
        self.timer_period = 1.0  # secondes
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.counter = 0
        self.get_logger().info('Number publisher started: publishing on /number every 1s')

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
