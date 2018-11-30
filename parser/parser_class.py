class CommandStructure():
    def __init__(self, parser_name=None):
        self.parser_name = parser_name

    def attribute_parser(self, parameters, cmd):
        pass

class SysGetStatus(CommandStructure):
    def __init__(self):
        self.cmd = None
        self.mac = None
        self.project_name = None
        self.cli_version  = None
        self.boost_version = None
        self.hw_version = None
        self.fw_version = None
        self.clock = None
        self.storage_capacity = None
        self.storage_last_capacity = None
        self.len = None
        super().__init__()   

    def attribute_parser(self, parameters, cmd):   
        self.cmd = cmd
        self.mac, self.project_name, self.cli_version, self.boost_version, self.hw_version, self.fw_version, \
        self.clock, self.storage_capacity, self.storage_last_capacity, self.len = (parameters.split(","))
        
class SysSetSystem(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.reset_num = None
        self.len = None
    
    def attribute_parser(self, parameters, cmd):   
        self.cmd = cmd
        self.reset_num, self.len = parameters.split(",")
        
class SysSetRtc(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.date = None
        self.len = None   
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.date, self.len = parameters.split(",")
        
class SysGetRtc(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.date = None
        self.len = None
        
    def attribute_parser(self, parameters, cmd):  
        self.cmd = cmd  
        self.date, self.len = parameters.split(",")
        
class SysSetUtc(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.date = None
        self.len = None
        self.time_zone = None
             
    def attribute_parser(self, parameters, cmd):
        self.cmd = cmd  
        self.date, self.time_zone, self.len = parameters.split(",")
          
class SysGetUtc(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.date = None
        self.len = None
        self.time_zone = None
              
    def attribute_parser(self, parameters, cmd):
        self.cmd = cmd  
        self.date, self.time_zone, self.len = parameters.split(",")
        

class SysGetRsoc(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        self.rsoc = None
        self.len = None      
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.rsoc, self.len = parameters.split(",")
        
class SysSetManufactureCode(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None
        
        self.password = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.password, self.len = parameters.split(",")

class SysGetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.counter_value = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.counter_value, self.len = parameters.split(",")

class SysSetResetCounter(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.set_counter_value = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.set_counter_value, self.len = parameters.split(",")

class SystSetSystemModetoBootMode(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.password = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.password, self.len = parameters.split(",")

class SysSetProjectMode(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.mode = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.mode, self.len = parameters.split(",")

class SysSetPersonalInformation(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.gender = None 
        self.height = None  
        self.weight = None 
        self.age = None
        self.len = None    
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        content, self.len = parameters.split(",")
        self.gender, self.height, self.weight, self.age = content.split()

class SysGetFileList(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.list_array = []
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        list_array, self.len = parameters.rsplit(",",1)
        for file_path in list_array.split(","):
            self.list_array.append(file_path)

class SysGetFileSize(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.file_size = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_size, self.len = parameters.split(",")

class SysGetFileContents(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.file_ = None 
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        self.file_size, self.len = parameters.split(",")

class SysGetFileContents(CommandStructure):
    def __init__(self):
        super().__init__()
        self.cmd = None  
        self.file_content = None 
        self.file_name = None
        self.file_start = None
        self.file_end = None
        self.len = None     
        
    def attribute_parser(self, parameters, cmd): 
        self.cmd = cmd  
        file_information, self.file_content = parameters.split("\n")
        self.file_name, self.file_start,self.file_end, self.len = file_information.split(",")



    