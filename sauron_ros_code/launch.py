from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        # Vision
        Node(package='vision', node_executable='allSeeingEye', output='screen'),

        # comms
        Node(package='comms', node_executable='ringWraithPub', output='screen'),
        Node(package='comms', node_executable='ringWraithSub', output='screen')

    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()