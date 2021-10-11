import sim,time,sys
sys.path.insert(0, "..")

class SimPuppy:
    '''创建对象后用self.IsReady查看是否成功'''
    def __init__(self):
        CoppeliaSim_IpAddress = "127.0.0.1" # 默认为本地地址
        sim.simxFinish(-1) # just in case, close all opened connections
        self.__clientID = sim.simxStart(CoppeliaSim_IpAddress,19999,True,True,5000,5) # Connect to CoppeliaSim
        if self.__IsReady():           
            self.__opMode = sim.simx_opmode_blocking
            self.__FL_Motor1 = sim.simxGetObjectHandle(self.__clientID, "Motor1_FL", self.__opMode)
            self.__FL_Motor2 = sim.simxGetObjectHandle(self.__clientID, "Motor2_FL", self.__opMode)
            self.__FL_Motor3 = sim.simxGetObjectHandle(self.__clientID, "Motor3_FL", self.__opMode)
            self.__FR_Motor1 = sim.simxGetObjectHandle(self.__clientID, "Motor1_FR", self.__opMode)
            self.__FR_Motor2 = sim.simxGetObjectHandle(self.__clientID, "Motor2_FR", self.__opMode)
            self.__FR_Motor3 = sim.simxGetObjectHandle(self.__clientID, "Motor3_FR", self.__opMode)
            self.__BL_Motor1 = sim.simxGetObjectHandle(self.__clientID, "Motor1_BL", self.__opMode)
            self.__BL_Motor2 = sim.simxGetObjectHandle(self.__clientID, "Motor2_BL", self.__opMode)
            self.__BL_Motor3 = sim.simxGetObjectHandle(self.__clientID, "Motor3_BL", self.__opMode)
            self.__BR_Motor1 = sim.simxGetObjectHandle(self.__clientID, "Motor1_BR", self.__opMode)
            self.__BR_Motor2 = sim.simxGetObjectHandle(self.__clientID, "Motor2_BR", self.__opMode)
            self.__BR_Motor3 = sim.simxGetObjectHandle(self.__clientID, "Motor3_BR", self.__opMode)            
            self.IsReady = True
        else:
            self.IsReady = False
        
    def __IsReady(self):
        if self.__clientID != -1:
            return True
        else:
            return False
        
    def SetV_FL1(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FL_Motor1, V, self.__opMode)        
    def SetV_FL2(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FL_Motor2, V, self.__opMode)
    def SetV_FL3(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FL_Motor3, V, self.__opMode)
        
    def SetV_FR1(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FR_Motor1, V, self.__opMode)
    def SetV_FR2(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FR_Motor2, V, self.__opMode)
    def SetV_FR3(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__FR_Motor3, V, self.__opMode)
        
    def SetV_BL1(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BL_Motor1, V, self.__opMode)        
    def SetV_BL2(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BL_Motor2, V, self.__opMode)
    def SetV_BL3(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BL_Motor3, V, self.__opMode)
        
    def SetV_BR1(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BR_Motor1, V, self.__opMode)        
    def SetV_BR2(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BR_Motor2, V, self.__opMode)
    def SetV_BR3(self, V):
        sim.simxSetJointTargetVelocity(self.__clientID, self.__BR_Motor3, V, self.__opMode)        

SimPuppy = SimPuppy()       
Update_Period = 0.01 # 数据更新周期,单位s
    
time.sleep(Update_Period)

opMode=sim.simx_opmode_blocking     # 设置操作模式，等待返回值模式
# 得到句柄
_, FL_Motor1 = sim.simxGetObjectHandle(clientID, "Motor1_FL", opMode)
_, FL_Motor2 = sim.simxGetObjectHandle(clientID, "Motor2_FL", opMode)
_, FL_Motor3 = sim.simxGetObjectHandle(clientID, "Motor3_FL", opMode)

motor_1_v = 0


'''
    sim.simxSetJointTargetVelocity(clientID, FL_Motor1, motor_1_v, opMode)
    # return position
    _, position_1 = sim.simxGetJointPosition(clientID, FL_Motor1, opMode)
    _, position_2 = sim.simxGetJointPosition(clientID, FL_Motor2, opMode)
    
    #设置力、目标位置     关闭Control loop后该设置无效，使用Control loop需要调节PID参数
    # sim.simxSetJointForce(clientID, motor1, 1e-01, opMode)    
    # sim.simxSetJointTargetPosition(clientID, motor1, -0.1, opMode)
'''