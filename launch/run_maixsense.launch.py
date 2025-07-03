from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Dichiarazione degli argomenti
    sim_environment_arg = DeclareLaunchArgument(
        'sim_environment',
        default_value='false',
        description='Use simulated environment (true = use_sim_time)'
    )

    device_arg = DeclareLaunchArgument(
        'device',
        default_value='/dev/ttyUSB0',
        description='Serial device path'
    )

    # Recupera gli argomenti
    sim_env = LaunchConfiguration('sim_environment')
    device = LaunchConfiguration('device')

    # Nodo ROS
    publisher_node = Node(
        package='sipeed_tof_ms_a010',
        executable='publisher',
        name='tof_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': sim_env},
            {'device': device}
        ]
    )

    return LaunchDescription([
        sim_environment_arg,
        device_arg,
        publisher_node
    ])
