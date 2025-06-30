from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Dichiarazione dell'argomento sim_environment
    sim_environment_arg = DeclareLaunchArgument(
        'sim_environment',
        default_value='false',
        description='Use simulated environment (true = use_sim_time)'
    )

    # Recupera il valore dell'argomento
    sim_env = LaunchConfiguration('sim_environment')

    # Nodo publisher con use_sim_time impostato dinamicamente
    publisher_node = Node(
        package='sipeed_tof_ms_a010',
        executable='publisher',
        name='tof_publisher',
        output='screen',
        parameters=[{'use_sim_time': sim_env}]
    )

    return LaunchDescription([
        sim_environment_arg,
        publisher_node
    ])
