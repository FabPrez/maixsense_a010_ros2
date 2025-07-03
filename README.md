# maixsense_a10_ros2
maixsense_a10_ros2 is a simplified and fixed version of the original MaixSense A10 ROS 2 package, adapted for ROS 2 Humble on Ubuntu 22.04.

## Initial configuration
To enable access to the serial ports used to read data from the sensor, first find the serial port with:
```bash
ls /dev/ttyUSB* o ls /dev/ttyACM*
```
Then enable the reading and writing of that port with:
```bash
sudo chmod 666 /dev/ttyUSB0
```

## Quick Start
You can launch the publisher node in either simulated or real environment using the sim_environment launch argument.

## Real Environment (default)
```bash
ros2 launch sipeed_tof_ms_a010 run_maixsense.launch.py device:=/dev/ttyUSB0
```

## Simulated Environment
```bash
ros2 launch sipeed_tof_ms_a010 run_maixsense.launch.py device:=/dev/ttyUSB0 sim_environment:=true
```
The sim_environment flag sets the use_sim_time parameter accordingly for proper integration with simulated ROS time.
