

DAT_LEN =  2
DAT_TYPE_LEN = 2
DAT_TIME_LEN = 2
DAT_HRB_LEN = 1
DAT_RRIB_LEN = 8
DAT_ACC_RAW_DATA_LEN = 600
DAT_GYR_RAW_DATA_LEN = 600
DAT_RESB_LEN = 1
DAT_ECG_RAW_DATA_LEN = 750
DAT_CNTB_LEN = 2
DAT_RSCB_LEN = 9
DAT_TEM_LEN = 2
DAT_POSTURE_LEN = 1
DAT_AF_LEN = 1



class DatParser():
    def __init__(self):
        self.len = None
        self.time_off_set = None
        self.hrb = b""
        self.rrib = b""
        self.acc = b""
        self.gyr = b""
        self.resb = b""
        self.ecg_raw_data = b""
        self.cntb = b""
        self.rscb = b""
        self.temperature = b""
        self.posture = b""
        self.af = b""
        
        self.motion_sample_rate = None
        self.motion_resolution = None
        self.acc_range = None
        self.gyr_range = None
        self.ecg_sample_rate = None
        self.ecg_adc_resolution = None
        self.ecg_adc_vref = None
        self.ecg_amp_gain = None
        self.ecg_amp_offset = None

    def setting_parameters(self, cmd_obj):
        global DAT_LEN 
        global DAT_TYPE_LEN 
        global DAT_TIME_LEN 
        global DAT_HRB_LEN 
        global DAT_RRIB_LEN 
        global DAT_ACC_RAW_DATA_LEN 
        global DAT_GYR_RAW_DATA_LEN 
        global DAT_RESB_LEN 
        global DAT_ECG_RAW_DATA_LEN 
        global DAT_CNTB_LEN 
        global DAT_RSCB_LEN 
        global DAT_TEM_LEN 
        global DAT_POSTURE_LEN 
        global DAT_AF_LEN 

        DAT_ACC_RAW_DATA_LEN = int(cmd_obj.motion_sample_rate * 3 * (cmd_obj.motion_resolution/8))
        DAT_GYR_RAW_DATA_LEN = int(cmd_obj.motion_sample_rate * 3 * (cmd_obj.motion_resolution/8))
        DAT_ECG_RAW_DATA_LEN = int(cmd_obj.ecg_sample_rate * (cmd_obj.ecg_adc_resolution/8))

        # self.motion_sample_rate = cmd_obj.motion_sample_rate
        # self.motion_resolution = cmd_obj.motion_resolution
        # self.acc_range = cmd_obj.acc_range
        # self.gyr_range = cmd_obj.gyr_range
        # self.ecg_sample_rate = cmd_obj.ecg_sample_rate
        # self.ecg_adc_resolution = cmd_obj.ecg_adc_resolution
        # self.ecg_adc_vref = cmd_obj.ecg_adc_vref
        # self.ecg_amp_gain = cmd_obj.ecg_amp_gain
        # self.ecg_amp_offset = cmd_obj.ecg_amp_offset     



    def distrubute_dat_data(self, data):
        data = data.split(b"+DAT:")[1]
        self.len = data[:DAT_LEN]     
        data = data[DAT_LEN:]
        data_type = data[:DAT_TYPE_LEN]
        type_int = int.from_bytes(data_type, byteorder="little")
        data = data[DAT_TYPE_LEN:]
        self.time_off_set = data[:DAT_TIME_LEN]
        data = data[DAT_TIME_LEN:]
        if type_int & (1 << 0):
            self.hrb += self.time_off_set
            self.hrb += data[:DAT_HRB_LEN]
            data = data[DAT_HRB_LEN:]
        if type_int & (1 << 1):
            self.rrib += self.time_off_set
            self.rrib += data[:DAT_RRIB_LEN]
            data = data[DAT_RRIB_LEN:]
        if type_int & (1 << 2):
            self.acc += self.time_off_set
            self.acc += data[:DAT_ACC_RAW_DATA_LEN]
            data = data[DAT_ACC_RAW_DATA_LEN:]
        if type_int & (1 << 3):
            self.gyr += self.time_off_set
            self.gyr += data[:DAT_GYR_RAW_DATA_LEN]
            data = data[DAT_GYR_RAW_DATA_LEN:]
        if type_int & (1 << 4):
            self.resb += self.time_off_set
            self.resb += data[:DAT_RESB_LEN]
            data = data[DAT_RESB_LEN:]
        if type_int & (1 << 5):
            self.ecg_raw_data += self.time_off_set
            self.ecg_raw_data += data[:DAT_ECG_RAW_DATA_LEN]
            data = data[DAT_ECG_RAW_DATA_LEN:]
        if type_int & (1 << 6):
            self.cntb += self.time_off_set
            self.cntb += data[:DAT_CNTB_LEN]
            data = data[DAT_CNTB_LEN:]
        if type_int &  (1 << 7):
            self.rscb += self.time_off_set
            self.rscb += data[:DAT_RSCB_LEN]
            data = data[DAT_RSCB_LEN:]
        if type_int &  (1 << 8):
            self.temperature += self.time_off_set
            self.temperature += data[:DAT_TEM_LEN]
            data = data[DAT_TEM_LEN:]

        if type_int & (1 << 9):
            self.posture += self.time_off_set
            self.posture += data[:DAT_POSTURE_LEN]
            data = data[DAT_POSTURE_LEN:]       
        if type_int & (1 << 10):
            self.af += self.time_off_set
            self.af = data[:DAT_AF_LEN]
            data = data[DAT_AF_LEN:]



# data = "120300112345678"
# byte_content = b"\r\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\n"
# fc = DatParser()
# content = b"+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n" 

# fc.distrubute_dat_data(content)

# print(fc.hrb)
# print(fc.rrib)
# print(fc.gyr)

# content = b"+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n" 
# print(content.split(b"+DAT:")[1])






