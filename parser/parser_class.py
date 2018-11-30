class CommandStructure():
    def __init__(self):
        self.cmd = None
        self.len = None
        
    def attribute_parser(self, parameters, cmd):
        pass

class SysGetStatus(CommandStructure):
    def __init__(self):       
        self.mac = None
        self.project_name = None
        self.cli_version  = None
        self.boost_version = None
        self.hw_version = None
        self.fw_version = None
        self.clock = None
        self.storage_capacity = None
        self.storage_last_capacity = None        
        super().__init__()   

    def attribute_parser(self, parameters, cmd):   
        self.cmd = cmd
        self.mac, self.project_name, self.cli_version, self.boost_version, self.hw_version, self.fw_version, \
        self.clock, self.storage_capacity, self.storage_last_capacity, self.len = (parameters.split(","))   

class SysSetSystem(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.reset_num = None
        
    def attribute_parser(self, parameters, cmd):   
        self.cmd = cmd
        self.reset_num, self.len = parameters.split(",")
        
class SysSetRtc(CommandStructure):
    def __init__(self):
        super().__init__()     
        self.date = None
              
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.date, self.len = parameters.split(",")
        
class SysGetRtc(CommandStructure):
    def __init__(self):
        super().__init__()    
        self.date = None
             
    def attribute_parser(self, parameters, cmd):  
        self.cmd = cmd  
        self.date, self.len = parameters.split(",")
        
class SysSetUtc(CommandStructure):
    def __init__(self):
        super().__init__()       
        self.date = None 
        self.time_zone = None
             
    def attribute_parser(self, parameters, cmd):
        self.cmd = cmd  
        self.date, self.time_zone, self.len = parameters.split(",")
          
class SysGetUtc(CommandStructure):
    def __init__(self):
        super().__init__()    
        self.date = None 
        self.time_zone = None
              
    def attribute_parser(self, parameters, cmd):
        self.cmd = cmd  
        self.date, self.time_zone, self.len = parameters.split(",")
        
class SysGetRsoc(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.rsoc = None
                  
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.rsoc, self.len = parameters.split(",")
        
class SysSetManufactureCode(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.password = None 
             
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.password, self.len = parameters.split(",")

class SysGetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__()       
        self.counter_value = None 
                    
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.counter_value, self.len = parameters.split(",")

class SysSetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.set_counter_value = None 
                
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.set_counter_value, self.len = parameters.split(",")

class SystSetSystemModetoBootMode(CommandStructure):
    def __init__(self):
        super().__init__()     
        self.password = None 
                  
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.password, self.len = parameters.split(",")

class SysSetProjectMode(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.mode = None 
                 
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.mode, self.len = parameters.split(",")

class SysSetPersonalInformation(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.gender = None 
        self.height = None  
        self.weight = None 
        self.age = None
              
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        content, self.len = parameters.split(",")
        self.gender, self.height, self.weight, self.age = content.split()

class SysGetFileList(CommandStructure):
    def __init__(self):
        super().__init__()
        self.list_array = []
                  
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        list_array, self.len = parameters.rsplit(",",1)
        for file_path in list_array.split(","):
            self.list_array.append(file_path)

class SysGetFileSize(CommandStructure):
    def __init__(self):
        super().__init__()      
        self.file_size = None 
               
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_size, self.len = parameters.split(",")

class SysGetFileContents(CommandStructure):
    def __init__(self):
        super().__init__()    
        self.file_ = None 
                
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_size, self.len = parameters.split(",")

class SysGetFileContents(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.file_content = None 
        self.file_name = None
        self.file_start = None
        self.file_end = None
             
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        file_information, self.file_content = parameters.split("\n")
        self.file_name, self.file_start,self.file_end, self.len = file_information.split(",")

class SysRemoveFile(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.file_name = None 
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_name, self.len = parameters.split(",")

class SysCreateTestFile(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.file_name = None 
        self.file_size = None
        self.file_content = None
               
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_name, self.file_size, self.file_content, self.len = parameters.split(",")

class SystGetBinaryRawData(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.type = None 
        # self.motion_id = None
        # self.motion_sensor_sample_rate = None
        # self.motion_sensor_resolution = None
        # self.acc_rang = None
        # self.gyto_rang = None
        # self.ecg_sample_rate = None
        # self.ecg_adc_resolution = None
        # self.ecg_adc_vref = None
        # self.ecg_amp_gain = None
        # self.ecg_amp_offset = None
        # self.adc_signed = None
        # self.user_gender = None
        # self.user_height = None
        # self.user_weight = None
        # self.user_age = None
        # self.reserve = None
        self.support_dic = {}
        self.val = {}   
              
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.type, content = parameters.split(",", 1)
        if self.type == "999":
            content, self.len = content.rsplit(",", 1)
            content_list = content.split(",")
            val_list = ["Motion sensor ID", "Motion sensor sample rate. Unit=Hz.", \
                        "Motion sensor resolution. Unit=bit.","Accelerometer rang. Unit=±g.", \
                        "Gyro range. Unit=±n°/s", "ECG sample rate. Unit=Hz", \
                        "ECG ADC Resolution. Unit=bit", "ECG ADC_Vref Unit=mV", \
                        "ECG AMP_Gain", "ECG AMP_offset Unit=mV", "ADC_Sign", "User gender", \
                        "User height", "User weight", "User age"]
            for x in val_list:
                self.val[x] = content_list[0]
                content_list.pop(0)    

        elif self.type == "998":
            content, self.len = content.split(",")
            b = bin(int(content, 16))[2:].zfill(16)
            support_list = ["Heart rate supported", "RR-Interval supported", "Accelerometer supported",
                            "Gyro scope supported", "Respiration supported", "ECG raw data supported",
                            "Pedometer step counter supported", "RSC data supported",
                            "Temperature supported", "Posture event supported",
                            "AF(Atrial fibrillation) supported"]
            b = list(b)
            for x in support_list:
                self.support_dic[x] = b[-1]
                b.pop()

        else:
            self.val, self.len = content.split(",")
                
class SystemStopSendBinaryRawData(CommandStructure):
    def __init__(self):
        super().__init__()
          
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.len = parameters        

class SystemStopSendBinaryRawDataWithCompression(CommandStructure):
    def __init__(self):
        super().__init__()          
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.len = parameters   

class SysSetPacketSizeOfECG(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.size = None        
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.size, self.len = parameters.split(",")

class SysGetPacketSizeOfECG(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.size = None        
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.size, self.len = parameters.split(",")

class SysStartCalibrationACC(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.sel = None        
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.sel, self.len = parameters.split(",")

class SysSetMotionDataRate(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.rate = None        
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.rate, self.len = parameters.split(",")

class SysGetSensorRange(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.type = None  
        self.range = None      
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        content, self.len = parameters.split(",")
        self.type, self.range = content.split(" ")

class SysSetSensorRange(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.type = None  
        self.range = None      
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        content, self.len = parameters.split(",")
        self.type, self.range = content.split(" ")


map_dic = {
        "CLI=get status": SysGetStatus(),
        "CLI=set reset": SysSetSystem(),
        "CLI=set RTC": SysSetRtc(),
        "CLI=get RTC": SysGetRtc(),
        "CLI=set UTC": SysSetUtc(),
        "CLI=get UTC": SysGetUtc(),
        "CLI=get SOC": SysGetRsoc(),
        "CLI= set MFG": SysSetManufactureCode(),
        "CLI= get ResetCounter": SysGetResetCounter(),
        "CLI= set ResetCounter": SysSetResetCounter(),
        "CLI=set boot": SystSetSystemModetoBootMode(),
        "CLI=set mode": SysSetProjectMode(),
        "CLI= set pi": SysSetPersonalInformation(),
        "CLI=get file_list": SysGetFileList(),
        "CLI=get file_size": SysGetFileSize(),
        "CLI=get file_contents": SysGetFileContents(),
        "CLI=rm file": SysRemoveFile(),
        "CLI=file_test": SysCreateTestFile(),
        "CLI=get dat_char": SystGetBinaryRawData(),
        "CLI=stop dat": SystemStopSendBinaryRawData(),
        "CLI=stop dat_cmp": SystemStopSendBinaryRawDataWithCompression(),
        "CLI=set dat_eps": SysSetPacketSizeOfECG(),
        "CLI=get dat_eps": SysGetPacketSizeOfECG(),
        "CLI=start calib": SysStartCalibrationACC(),
        "CLI=set odr": SysSetMotionDataRate(),
        "CLI=get range": SysGetSensorRange(),
        "CLI=set range": SysSetSensorRange()
         }
                   
            





    