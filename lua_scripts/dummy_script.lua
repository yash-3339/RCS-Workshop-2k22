function sysCall_init()
    -- do some initialization here
    h1 = sim.getObject('/revolute_1')
    h2 = sim.getObject('/revolute_2')
    h3 = sim.getObject('/revolute_3')
    h4 = sim.getObject('/revolute_4')
    
    vl = 0
    vc = 0
    r = 0.5
end

function sysCall_actuation()
    -- put your actuation code here
    if simROS then
        sim.addLog(sim.verbosity_scriptinfos, "ROS Interface Found")
        
        sub = simROS.subscribe('/cmd_vel', 'geometry_msgs/Twist', 'Message_callback')
        -- simROS.subscriberTreatUInt8ArayAsString(sub)
    end
    
    function Message_callback(vel)
        vl = vel.linear.x - r*vel.angular.z  
        vc = vel.linear.x + r*vel.angular.z

        sim.setJointTargetVelocity(h1, vl)
        sim.setJointTargetVelocity(h2, vc)
        sim.setJointTargetVelocity(h3, vc)
        sim.setJointTargetVelocity(h4, vl)
    end

end

function sysCall_sensing()
    -- put your sensing code here

end

function sysCall_cleanup()
    -- do some clean-up here
    if simROS then
        simROS.shutdownSubscriber(sub)
    end
end

-- See the user manual or the available code snippets for additional callback functions and details
