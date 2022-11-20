# This #Tutorial introduces the user to the Basics of ROS.
Inorder to work with **ROS** a **ROS_workspace** has to be created in your system where all the necessary dependencies and libraries which are required to run the roscripts would be initialized (analogy: To work with electronics we need tools to handle electronics ).
## Creating a ROS workspace:
#### In order to create a Ros_workspace a new_directory has to be created with a src directory inside it.
```
mkdir -p ~/catkin_ws/src
```
Now to make this  directory loaded with all the ros tools which we would require to work with rosscripts.
Navigate to the ros_ws
```
cd ~/catkin_ws
```
Now we have to catkin_make it  to build all the packages which we would require inorder to work with ROS.
```
catkin_make
```
After catkin_make you could find ***build*** ,***devel*** and ***src/Cmakelists.txt*** files would be created in your workspace.
