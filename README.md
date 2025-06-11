#maixsense_a10_ros2
maixsense_a10_ros2 is a simplified and fixed version of the original MaixSense A10 ROS 2 package, adapted for ROS 2 Humble on Ubuntu 22.04.

# Quick start
To enable access to the serial ports used to read data from the sensor, run the following commands before launching the node:

```bash
sudo chmod 666 /dev/ttyUSB1
sudo chmod 666 /dev/ttyUSB0
```
