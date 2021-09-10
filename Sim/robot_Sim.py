import sim,time,sys
sys.path.insert(0, "..")

Update_Period = 0.01#数据更新周期,单位s
CoppeliaSim_IpAddress = "127.0.0.1"#默认为本地地址
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart(CoppeliaSim_IpAddress,19999,True,True,5000,5) # Connect to CoppeliaSim

while clientID!=-1:
    
    time.sleep(Update_Period)
    
    opMode=sim.simx_opmode_blocking     # 设置操作模式，等待返回值模式
    '''得到句柄'''
    ret1, motor1 = sim.simxGetObjectHandle(clientID, "Motor_1", opMode)
    ret2, motor2 = sim.simxGetObjectHandle(clientID, "Motor_2", opMode)
    ret3, motor3 = sim.simxGetObjectHandle(clientID, "Motor_3", opMode)
    
    motor_1_v = 0
    
    sim.simxSetJointTargetVelocity(clientID, motor1, motor_1_v, opMode)
    
    # return position
    _, position_1 = sim.simxGetJointPosition(clientID, motor1, opMode)
    _, position_2 = sim.simxGetJointPosition(clientID, motor2, opMode)
    
    '''设置力、目标位置     关闭Control loop后该设置无效，使用Control loop需要调节PID参数'''
    # sim.simxSetJointForce(clientID, motor1, 1e-01, opMode)    
    # sim.simxSetJointTargetPosition(clientID, motor1, -0.1, opMode)    