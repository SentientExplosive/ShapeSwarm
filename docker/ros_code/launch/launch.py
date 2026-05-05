from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        # brian
        Node(package='brian_pkg',
             namespace='brian',
             executable='brian',
             output='screen'
        ),

        # eyeComms
        Node(package='eyeComms_pkg', 
             namespace='ringWraithPub',
             executable='ringWraithPub',
             output='screen'
        ),
        Node(package='eyeComms_pkg',
             namespace='ringWraithSub',
             executable='ringWraithSub',
             output='screen'
        ),

        # megaComms
        Node(package='megaComms_pkg',
             namespace='megaComms',
             executable='megaComms',
             output='screen'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()