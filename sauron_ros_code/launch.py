from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        # vision_pkg
        Node(package='vision_pkg',
             namespace='allSeeingEye',
             executable='allSeeingEye',
             output='screen'),

        # comms_pkg
        Node(package='comms_pkg',
             namespace='ringWraithPub',
             executable='ringWraithPub',
             output='screen'),
        Node(package='comms_pkg',
             namespace='ringWraithSub',
             executable='ringWraithSub',
             output='screen')

    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()