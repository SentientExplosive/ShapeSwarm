from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        # brian
        Node(package='brian_pkg', node_executable='brian', output='screen'),

        # eyeComms
        Node(package='eyeComms_pkg', node_executable='ringWraithPub', output='screen'),
        Node(package='eyeComms_pkg', node_executable='ringWraithSub', output='screen'),

        # megaComms
        Node(package='megaComms_pkg', node_executable='megaComms', output='screen')
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()