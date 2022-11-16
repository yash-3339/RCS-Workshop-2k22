# RCS-Workshop-2k22

In this workshop you'll learn to manoeuvre the previously designed Mobile Robot in **Copeliasim V4.3** Simulation Software.

Implement the following commands in your Ubuntu 20.04 terminal to setup your system.

## Prerequisites/Dependencies
* Laptop with Ubuntu 20.04 booted in it.
* ROS Noetic
* Coppeliasim V4.3 

## Run the project  
* Clone this repository in your home folder
```
git clone https://github.com/KarthikMothiki/RCS-Workshop-2k22.git
```
* Open the repository, make and source  
```
cd /catkin_ws/
catkin_make
source devel/setup.bash
```

## Testing the System Setup
1. ROS Version
```
rosversion -d
```
Upon typing this command, **"noetic"** must be printed in the terminal

2. Updating the packages
```
sudo apt-get update -y
```
3. Upgrading the packages
```
sudo apt upgrade -y
```
4. If you want to finish both in same command, then make use of this command
```
sudo apt-get update && sudo apt upgrade -y
```

## Opening the simulation 

1. Master
```
roscore
```

2. Coppeliasim
Go to the path where Coppeliasim software is present and type the following command
```
./coppeliasim.sh
```
This should launch the Coppeliasim application

3. Movement of the Robot
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

Generally teleop_twist_keyboard will be pre-instlled in the ROS installation procedure. But if you run into some error while launching, there are two easiest and common methods to troubleshoot this issue.

1. Check whether the package is installed in some other directory and delete the package in that directory.
2. Check whether the package is present in /opt/ros/noetic/lib path and the **teleop_twist_keyboard.py** file is executable.
-- If it isn't, run the following commands
```
cd /opt/ros/noetic/lib/teleop_twist_keyboard
sudo chmod +x teleop_twist_keyboar.py
```
This should do the work.
