import cmd_type
import dat_parser



class CliResponseParser():
    def __init__(self):
        self.type_int = None
        self.cmd = None
        self.parameters = None    
        self.type_key = None
            
           
    def mapping_parser(self, cmd, parameters, parser_type):
        parser_object = create_parser(parser_type)
        
        parser_object.attribute_parser(parameters, cmd)
        return parser_object       

    def cli_cmd(self, input_repsonse):
        
        self.cmd, self.parameters = input_repsonse.split(b":", 1)
        self.type_key = self.cmd.split(b"=")[1] 
        

        self.type_int = cmd_type.CMD_STRING_MAP.get(self.type_key)

    def create_cmd_parser(self, input_repsonse):
        self.cli_cmd(input_repsonse)
        new_cmd_parser = self.mapping_parser(self.type_key, self.parameters, self.type_int)
        
        return new_cmd_parser







class CommandStructure():
    def __init__(self):
        self.type_key = None
        self.len = None
        
    def attribute_parser(self, parameters, type_key):
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

    def attribute_parser(self, parameters, type_key):   
        self.type_key = type_key 
        self.mac, self.project_name, self.cli_version, self.boost_version, self.hw_version, self.fw_version, \
        self.clock, self.storage_capacity, self.storage_last_capacity, self.len = (parameters.split(b","))   

class SysSetSystem(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.reset_num = None
        
    def attribute_parser(self, parameters, type_key):   
        self.type_key = type_key
        self.reset_num, self.len = parameters.split(b",")
        
class SysSetRtc(CommandStructure):
    def __init__(self):
        super().__init__()     
        self.date = None
              
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.date, self.len = parameters.split(b",")
        
class SysGetRtc(CommandStructure):
    def __init__(self):
        super().__init__()    
        self.date = None
             
    def attribute_parser(self, parameters, type_key):  
        self. type_key = type_key  
        self.date, self.len = parameters.split(b",")
        
class SysSetUtc(CommandStructure):
    def __init__(self):
        super().__init__()       
        self.date = None 
        self.time_zone = None
             
    def attribute_parser(self, parameters, type_key):
        self. type_key = type_key  
        self.date, self.time_zone, self.len = parameters.split(b",")
          
class SysGetUtc(CommandStructure):
    def __init__(self):
        super().__init__()    
        self.date = None 
        self.time_zone = None
              
    def attribute_parser(self, parameters, type_key):
        self. type_key = type_key  
        self.date, self.time_zone, self.len = parameters.split(b",")
        
class SysGetRsoc(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.rsoc = None
                  
    def attribute_parser(self, parameters, type_key): 
        self. type_key = type_key  
        self.rsoc, self.len = parameters.split(b",")
        
class SysSetManufactureCode(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.password = None 
             
    def attribute_parser(self, parameters, type_key): 
        self. type_key = type_key  
        self.password, self.len = parameters.split(b",")

class SysGetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__()       
        self.counter_value = None 
                    
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.counter_value, self.len = parameters.split(b",")

class SysSetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.set_counter_value = None 
                
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.set_counter_value, self.len = parameters.split(b",")

class SystSetSystemModetoBootMode(CommandStructure):
    def __init__(self):
        super().__init__()     
        self.password = None 
                  
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.password, self.len = parameters.split(b",")

class SysSetProjectMode(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.mode = None 
                 
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.mode, self.len = parameters.split(b",")

class SysSetPersonalInformation(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.gender = None 
        self.height = None  
        self.weight = None 
        self.age = None
              
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        content, self.len = parameters.split(b",")
        self.gender, self.height, self.weight, self.age = content.split()

class SysGetPersonalInformation(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.gender = None 
        self.height = None  
        self.weight = None 
        self.age = None
              
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        content, self.len = parameters.split(b",")
        self.gender, self.height, self.weight, self.age = content.split()

class SysGetFileList(CommandStructure):
    def __init__(self):
        super().__init__()
        self.list_array = []
                  
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        list_array, self.len = parameters.rsplit(b",",1)
        for file_path in list_array.split(b","):
            self.list_array.append(file_path)

class SysGetFileSize(CommandStructure):
    def __init__(self):
        super().__init__()      
        self.file_size = None 
               
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.file_size, self.len = parameters.split(b",")

class SysGetFileContents(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.file_content = None 
        self.file_name = None
        self.file_start = None
        self.file_end = None
             
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        file_information, self.file_content = parameters.split(b"\n")
        self.file_name, self.file_start,self.file_end, self.len = file_information.split(b",")

class SysRemoveFile(CommandStructure):
    def __init__(self):
        super().__init__() 
        self.file_name = None 
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.file_name, self.len = parameters.split(b",")

class SysCreateTestFile(CommandStructure):
    def __init__(self):
        super().__init__()   
        self.file_name = None 
        self.file_size = None
        self.file_content = None
               
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.file_name, self.file_size, self.file_content, self.len = parameters.split(b",")

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
              
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.type, content = parameters.split(b",", 1)
        if self.type == b"999":
            content, self.len = content.rsplit(b",", 1)
            content_list = content.split(b",")
            val_list = ["Motion sensor ID", "Motion sensor sample rate. Unit=Hz.", \
                        "Motion sensor resolution. Unit=bit.","Accelerometer rang. Unit=±g.", \
                        "Gyro range. Unit=±n°/s", "ECG sample rate. Unit=Hz", \
                        "ECG ADC Resolution. Unit=bit", "ECG ADC_Vref Unit=mV", \
                        "ECG AMP_Gain", "ECG AMP_offset Unit=mV", "ADC_Sign", "User gender", \
                        "User height", "User weight", "User age"]
            for x in val_list:
                self.val[x] = content_list[0]
                content_list.pop(0)    

        elif self.type == b"998":
            content, self.len = content.split(b",")
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
            self.val, self.len = content.split(b",")
                
class SysStopSendBinaryRawData(CommandStructure):
    def __init__(self):
        super().__init__()
          
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.len = parameters  

class SysStartSendBinaryRawDataWithCompression(CommandStructure): 
    def __init__(self):
        super().__init__()          
        self.char = None
        self.type = None
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.type, self.char, self.len = parameters.split(b",")       

class SysStopSendBinaryRawDataWithCompression(CommandStructure):
    def __init__(self):
        super().__init__()          
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.len = parameters   

class SysSetPacketSizeOfECG(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.size = None        
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.size, self.len = parameters.split(b",")

class SysGetPacketSizeOfECG(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.size = None        
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.size, self.len = parameters.split(b",")

class SysStartCalibrationACC(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.sel = None        
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.sel, self.len = parameters.split(b",")

class SysSetMotionDataRate(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.rate = None        
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        self.rate, self.len = parameters.split(b",")

class SysGetSensorRange(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.type = None  
        self.range = None      
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        content, self.len = parameters.split(b",")
        self.type, self.range = content.split(b" ")

class SysSetSensorRange(CommandStructure):
    def __init__(self):
        super().__init__()  
        self.type = None  
        self.range = None      
        
    def attribute_parser(self, parameters, type_key): 
        self.type_key = type_key  
        content, self.len = parameters.split(b",")
        self.type, self.range = content.split(b" ")

class SysStartSendRawData(CommandStructure):
    def __init__(self):
        self.type = None    
        self.motion_id = None
        self.motion_sample_rate = None
        self.motion_resolution = None
        self.acc_range = None
        self.gyr_range = None
        self.ecg_sample_rate = None
        self.ecg_adc_resolution = None
        self.ecg_adc_vref = None
        self.ecg_amp_gain = None
        self.ecg_amp_offset = None
        self.signed = None
        self.user_gender = None
        self.user_height = None
        self.user_weight = None
        self.user_age = None

    def attribute_parser(self, parameters, type_key):
        self.type_key = type_key
        self.type, characters = parameters.split(b",", 1)
        type_int = int(self.type, 16)

        if not (type_int & (1 << 2)) and not(type_int & (1 << 3)) \
            and not (type_int & (1<<5)) and not (type_int & (1<<7)):
            self.len = characters
                      
        else:
            print("y")  
            if (type_int & (1 << 2)) and (type_int & (1 << 3)):
                print("a")
                self.char = characters.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.motion_sample_rate = int(self.char.pop(0))
                self.motion_resolution = int(self.char.pop(0))
                self.acc_range = int(self.char.pop(0))
                self.gyr_range = int(self.char.pop(0))
                # char_list = [self.motion_id, self.montion_sample_rate, \
                #              self.motion_resolution, self.acc_range, self.gyr_range]
                
                # for char in char_list:
                #     char = int(self.char.pop[0])                 
                                 
                
            elif (type_int & (1 << 2)) and not (type_int & (1 << 3)):
                print("b")
                self.char = characters.split(",")
                self.char = characters.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.motion_sample_rate = int(self.char.pop(0))
                self.motion_resolution = int(self.char.pop(0))
                self.acc_range = int(self.char.pop(0))
                
                # char_list = [self.motion_id, self.montion_sample_rate, \
                #              self.motion_resolution, self.acc_range]
                # for x in char_list:
                #     x = self.char.pop(0)
            elif (type_int & (1 << 3)) and not (type_int ^ (1 << 2)):
                print("c")
                self.char = characters.split(",")
                self.char = characters.split(b",")            
                self.motion_id = int(self.char.pop(0))
                self.motion_sample_rate = int(self.char.pop(0))
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

    # def create_dat_parser(self):
        
    #     parser_object = dat_parser_factory.Factory()
        
    #     data_list = self.dat_data.split(b"+DAT:")
    #     for x in data_list:  
    #         parser_object.distrubute_dat_data(x)

    #     return parser_object


def create_parser(type_key):
    if type_key == cmd_type.CmdType.GET_STATUS:
        return SysGetStatus()
    elif type_key == cmd_type.CmdType.SET_RESET:
        return SysSetSystem()
    elif type_key == cmd_type.CmdType.SET_RTC:
        return SysSetRtc()
    elif type_key == cmd_type.CmdType.GET_RTC: 
        return SysGetRtc()
    elif type_key == cmd_type.CmdType.SET_UTC:
        return SysSetUtc()
    elif type_key == cmd_type.CmdType.GET_UTC:
        return SysGetUtc()
    elif type_key == cmd_type.CmdType.GET_SOC:
        return SysGetRsoc()
    elif type_key == cmd_type.CmdType.SET_MFG:
        return SysSetManufactureCode()
    elif type_key == cmd_type.CmdType.GET_RESETCOUNTER:
        return SysGetResetCounter()
    elif type_key == cmd_type.CmdType.SET_RESETCOUNTER:
        return SysSetResetCounter()
    elif type_key == cmd_type.CmdType.SET_BOOT:
        return SystSetSystemModetoBootMode()
    elif type_key == cmd_type.CmdType.SET_MODE:
        return SysSetProjectMode()
    elif type_key == cmd_type.CmdType.SET_PI:
        return SysSetPersonalInformation()
    elif type_key == cmd_type.CmdType.GET_PI:
        return SysGetPersonalInformation()
    elif type_key == cmd_type.CmdType.GET_FILE_LIST:
        return SysGetFileList()
    elif type_key == cmd_type.CmdType.GET_FILE_SIZE:
        return SysGetFileSize()
    elif type_key == cmd_type.CmdType.GET_FILE_CONTENTS:
        return SysGetFileContents()
    elif type_key == cmd_type.CmdType.REMOVE:
        return SysRemoveFile()
    elif type_key == cmd_type.CmdType.FILE_TEST:
        return SysCreateTestFile()
    elif type_key == cmd_type.CmdType.GET_DAT_CHAR:
        return SystGetBinaryRawData()
    elif type_key == cmd_type.CmdType.START_DAT:
        return SysStartSendRawData()
    elif type_key == cmd_type.CmdType.STOP_DAT:
        return SysStopSendBinaryRawData()
    elif type_key == cmd_type.CmdType.START_DAT_CMP:
        return SysStartSendBinaryRawDataWithCompression()
    elif type_key == cmd_type.CmdType.STOP_DAT_CMP:
        return SysStopSendBinaryRawDataWithCompression()
    elif type_key == cmd_type.CmdType.SET_DAT_EPS:
        return SysSetPacketSizeOfECG()
    elif type_key == cmd_type.CmdType.GET_DAT_EPS:
        return SysGetPacketSizeOfECG()
    elif type_key == cmd_type.CmdType.START_CALIB:
        return SysStartCalibrationACC()
    elif type_key == cmd_type.CmdType.SET_ODR:
        return SysSetMotionDataRate()
    elif type_key == cmd_type.CmdType.GET_RANGE:
        return SysGetSensorRange()
    elif type_key == cmd_type.CmdType.SET_RANGE:
        return SysSetSensorRange()
    






                   
            
# content = b"CLI=start dat:077f,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,65\r\n"
# # cmd_content = b"CLI=get dat_char:999,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,1,180,70,25,79"
# cmd_fac = CliResponseParser()

# obj = cmd_fac.create_cmd_parser(content)
# # dat_data = b"+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n"
# dat_000c_data = b"+DAT:0\x01\x0c\x00\x00\x00Z\n\xc4\x15\xc1\x06.\n\xc9\x15\xa6\x06\x1e\n8\x16\\\x06@\n\xe3\x15q\x06O\n0\x16}\x06\x16\n\x9f\x16{\x06\xf3\t \x16]\x06\xc4\tq\x16!\x06\x91\t\xaa\x16D\x06\x13\n9\x16&\x06N\tG\x16\xd5\x05X\t\x95\x16V\x06\xc2\t\x98\x16O\x06X\t\x83\x16\xcd\x05h\t\x93\x16`\x064\t\xa6\x16\xfc\x05h\t\xd4\x16\xf9\x05g\t\xd4\x16c\x05\xd3\x08$\x17\x13\x06E\t5\x17\xfe\x05\xf5\x08\'\x17\x9a\x05Q\t@\x17\xeb\x05G\tb\x17\xd0\x05\x04\t\xca\x16\xc9\x05\xdf\x08\xfe\x16h\x054\x00\x7f\xff\xd8\xff6\x00u\xff\xd6\xff+\x00{\xff\xd1\xff0\x00\x80\xff\xdc\xff4\x00\x7f\xff\xcf\xff/\x00z\xff\xd8\xff6\x00}\xff\xd8\xff:\x00{\xff\xdc\xff1\x00z\xff\xd7\xff4\x00z\xff\xdc\xff8\x00y\xff\xdd\xff.\x00{\xff\xde\xff4\x00t\xff\xd9\xff3\x00y\xff\xdd\xff4\x00}\xff\xd0\xff;\x00w\xff\xdd\xff5\x00z\xff\xda\xff7\x00~\xff\xda\xff0\x00x\xff\xda\xff,\x00z\xff\xe0\xff#\x00v\xff\xe1\xff\x1c\x00~\xff\xe7\xff$\x00~\xff\xe7\xff\x02\x00y\xff\xf7\xff0\x00x\xff\xdb\xff\r\n"
# import dat_parser
# data_parser = dat_parser.DatParser()
# data_parser.setting_parameters(obj)
# data_parser.distrubute_dat_data(dat_000c_data)

# # print(obj.val)
# # print(obj.motion_sample_rate)
# # print(obj.motion_resolution)

# print(data_parser.hrb)
# print(data_parser.rrib)
# print("Acc:",data_parser.acc)
# print("ACC lenth:", len(data_parser.acc))
# print("Gyr:",data_parser.gyr)



    