#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class TurtleSquare(Node):
    """
    Fait dessiner un carré à la tortue en envoyant des commandes Twist.
    """
    def __init__(self):
        super().__init__('turtle_square')

        # Publisher pour /turtle1/cmd_vel
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.get_logger().info("Turtle square node started!")
        
        # Lance la procédure de dessin
        time.sleep(1.0)  # petite pause pour laisser turtlesim démarrer
        self.draw_square()


    def move_forward(self, distance, speed=1.0):
        """
        Avancer en ligne droite sur 'distance' mètres.
        """
        msg = Twist()
        msg.linear.x = speed
        
        # durée = distance / vitesse
        duration = distance / speed
        end_time = time.time() + duration
        
        self.get_logger().info(f"Moving forward for {duration:.2f} seconds")
        
        while time.time() < end_time:
            self.cmd_pub.publish(msg)
            time.sleep(0.01)

        # stop
        msg.linear.x = 0.0
        self.cmd_pub.publish(msg)


    def turn(self, angle_deg, speed=1.0):
        """
        Tourner en place d'un angle donné (en degrés).
        """
        msg = Twist()
        msg.angular.z = speed  # rad/s

        # convertir l’angle en radians
        angle_rad = math.radians(angle_deg)
        duration = angle_rad / speed
        end_time = time.time() + duration

        self.get_logger().info(f"Turning {angle_deg}° for {duration:.2f} seconds")

        while time.time() < end_time:
            self.cmd_pub.publish(msg)
            time.sleep(0.01)

        # stop
        msg.angular.z = 0.0
        self.cmd_pub.publish(msg)


    def draw_square(self):
        """
        Effectue 4 côtés + 4 rotations de 90°.
        """
        for i in range(4):
            self.get_logger().info(f"--- Side {i+1} ---")
            self.move_forward(2.0, speed=1.0)   # avancer 2 mètres
            self.turn(90, speed=1.0)            # tourner 90°


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
