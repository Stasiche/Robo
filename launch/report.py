from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            parameters=[{'background_r': 255,'background_b': 0,'background_g': 0}]
        )
    ])
