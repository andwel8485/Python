
class Factory():
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


    def distrubute_dat_data(self, data):
        data = data.split(b"+DAT:")[1]
        self.len = data[:2]     
        data = data[2:]
        data_type = data[:2]
        type_int = int.from_bytes(data_type, byteorder="little")
        data = data[2:]
        self.time_off_set = data[:2]
        data = data[2:]
        if type_int & (1 << 0):
            self.hrb += self.time_off_set
            self.hrb += data[:1]
            data = data[1:]
        if type_int & (1 << 1):
            self.rrib += self.time_off_set
            self.rrib += data[:8]
            data = data[8:]
        if type_int & (1 << 2):
            self.acc += self.time_off_set
            self.acc += data[:150]
            data = data[150:]
        if type_int & (1 << 3):
            self.gyr += self.time_off_set
            self.gyr += data[:150]
            data = data[150:]
        if type_int & (1 << 4):
            self.resb += self.time_off_set
            self.resb += data[:1]
            data = data[1:]
        if type_int & (1 << 5):
            self.ecg_raw_data += self.time_off_set
            self.ecg_raw_data += data[:750]
            data = data[750:]
        if type_int & (1 << 6):
            self.cntb += self.time_off_set
            self.cntb += data[:2]
            data = data[2:]
        if type_int &  (1 << 7):
            self.rscb += self.time_off_set
            self.rscb += data[:9]
            data = data[9:]
        if type_int &  (1 << 8):
            self.temperature += self.time_off_set
            self.temperature += data[:2]
            data = data[2:]

        if type_int & (1 << 9):
            self.posture += self.time_off_set
            self.posture += data[:1]
            data = data[1:]       
        if type_int & (1 << 10):
            self.af += self.time_off_set
            self.af = data[:1]
            data = data[1:]



# data = "120300112345678"
# byte_content = b"\r\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\n"
fc = Factory()
content = b"+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n" 

fc.distrubute_dat_data(content)

print(fc.hrb)
print(fc.rrib)
print(fc.gyr)

# content = b"+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n" 
# print(content.split(b"+DAT:")[1])






