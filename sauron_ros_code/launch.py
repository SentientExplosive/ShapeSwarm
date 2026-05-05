from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        # Vision
        Node(package='vision_pkg',
             namespace='allSeeingEye',
             executable='allSeeingEye',
             output='screen'),

        # comms
        Node(package='comms',
             namespace='ringWraithPub',
             executable='ringWraithPub',
             output='screen'),
        Node(package='comms',
             namespace='ringWraithSub',
             executable='ringWraithSub',
             output='screen')

    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()