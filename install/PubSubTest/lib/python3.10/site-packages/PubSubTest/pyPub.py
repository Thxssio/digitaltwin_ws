import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):

    def __init__(self):
        super().__init__('Test_Sub_Node')
        self.publisher = self.create_publisher(String, 'talker', 10)
        timer_period = 0.5 
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        message = String()
        message.data = 'Digital_Twin'
        self.publisher.publish(message)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = TalkerNode()
    rclpy.spin(minimal_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
