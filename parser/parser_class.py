import parser_type
import dat_parser_factory


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

class SysSendRawData(CommandStructure):
    def __init__(self):
        self.type = None
        self.char = None     
        self.dat_data = None
        self.motion_id = None
        self.montion_sample_rate = None
        self.motion_resolution = None
        self.acc_range = None
        self.gyr_range = None
        self.signed = None
        self.user_gender = None
        self.user_height = None
        self.user_weight = None
        self.user_age = None

    def attribute_parser(self, parameters, cmd):
        
        character, self.dat_data = parameters.split(b"\r\n+DAT:", 1) 
        self.type, character = character.split(b",", 1)
        type_int = int(self.type, 16)
                
        if not (type_int & (1 << 2)) and not(type_int & (1 << 3)) \
            and not (type_int & (1<<5)) and not (type_int & (1<<7)):
            self.len = character
                      
        else:
            print("y")  
            if (type_int & (1 << 2)) and (type_int & (1 << 3)):
                print("a")
                self.char = character.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.montion_sample_rate = int(self.char.pop(0))
                self.motion_resolution = int(self.char.pop(0))
                self.acc_range = int(self.char.pop(0))
                self.gyr_range = int(self.char.pop(0))
                # char_list = [self.motion_id, self.montion_sample_rate, \
                #              self.motion_resolution, self.acc_range, self.gyr_range]
                
                # for char in char_list:
                #     char = int(self.char.pop[0])                 
                                 
                
            elif (type_int & (1 << 2)) and not (type_int & (1 << 3)):
                print("b")
                self.char = character.split(",")
                self.char = character.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.montion_sample_rate = int(self.char.pop(0))
                self.motion_resolution = int(self.char.pop(0))
                self.acc_range = int(self.char.pop(0))
                
                # char_list = [self.motion_id, self.montion_sample_rate, \
                #              self.motion_resolution, self.acc_range]
                # for x in char_list:
                #     x = self.char.pop(0)
            elif (type_int & (1 << 3)) and not (type_int ^ (1 << 2)):
                print("c")
                self.char = character.split(",")
                self.char = character.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.montion_sample_rate = int(self.char.pop(0))
                self.motion_resolution = int(self.char.pop(0))
                self.gyr_range = int(self.char.pop(0))

                # char_list = [self.motion_id, self.montion_sample_rate, \
                #              self.motion_resolution,  self.gyr_range]
                # for x in char_list:
                #     x = self.char.pop(0)
            if type_int & (1 << 5):
                print("d")

                self.ecg_sample_rate = int(self.char.pop(0))
                self.ecg_adc_resolution = int(self.char.pop(0))
                self.ecg_adc_vref = int(self.char.pop(0))
                self.ecg_amp_gain = (self.char.pop(0))
                self.ecg_amp_offset = (self.char.pop(0))
                self.signed = int(self.char.pop(0))

                # char_list = [self.ecg_sample_rate, self.ecg_adc_resolution, self.ecg_adc_vref, \
                #              self.ecg_amp_gain, self.ecg_amp_offset, self.signed]
                # for x in char_list:
                #     x = self.char.pop(0)
                # print("char_list_int_ecg:", self.char)

            if type_int & (1 << 7):
                print("f")
                self.user_gender = int(self.char.pop(0))
                self.user_height = int(self.char.pop(0))
                self.user_weight = int(self.char.pop(0))
                self.user_age = int(self.char.pop(0))

                # char_list = [self.user_gender, self.user_height, \
                #              self.user_weight, self.user_age]
                # for x in char_list:
                #     x = self.char.pop(0)

    def create_dat_parser(self):
        
        parser_object = dat_parser_factory.Factory()
        
        data_list = self.dat_data.split(b"+DAT:")
        for x in data_list:  
            parser_object.distrubute_dat_data(x)

        return parser_object


def create_parser(cmd):
    if cmd == 1:
        return SysGetStatus()
    elif cmd == 2:
        return SysSetSystem()
    elif cmd == 3:
        return SysSetRtc()
    elif cmd == 4: 
        return SysSetRtc()
    elif cmd == 5:
        return SysSetUtc()
    elif cmd == 6:
        return SysGetUtc()
    elif cmd == 7:
        return SysGetRsoc()
    elif cmd == 8:
        return SysSetManufactureCode()
    elif cmd == 9:
        return SysGetResetCounter()
    elif cmd == 10:
        return SysSetResetCounter()
    elif cmd == 11:
        return SystSetSystemModetoBootMode()
    elif cmd == 12:
        return SysSetProjectMode()
    elif cmd == 13:
        return SysSetPersonalInformation()
    elif cmd == 14:
        return SysGetFileList()
    elif cmd == 15:
        return SysGetFileSize()
    elif cmd == 16:
        return SysGetFileContents()
    elif cmd == 17:
        return SysRemoveFile()
    elif cmd == 18:
        return SysCreateTestFile()
    elif cmd == 19:
        return SystGetBinaryRawData()
    elif cmd == 20:
        return SystemStopSendBinaryRawData()
    elif cmd == 21:
        return SystemStopSendBinaryRawDataWithCompression()
    elif cmd == 22:
        return SysSetPacketSizeOfECG()
    elif cmd == 23:
        return SysGetPacketSizeOfECG()
    elif cmd == 24:
        return SysStartCalibrationACC()
    elif cmd == 25:
        return SysSetMotionDataRate()
    elif cmd == 26:
        return SysGetSensorRange()
    elif cmd == 27:
        return SysSetSensorRange()
    elif cmd == 28:
        return SysSendRawData()



                   
            





    