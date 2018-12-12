import parser_frame
import threading 


CMD_LIST = []
DAT_LIST = []
TIMER = None




class CmdFrame():
    def __init__(self, cmd):
        self.type_key = cmd
        self.cmd_response_obj = None


        
def store_cmd(cmd):   #for UI
    global CMD_LIST
    global TIMER
    print("In store command func")
    new_cmd_obj = CmdFrame(cmd)
    CMD_LIST.append(new_cmd_obj)
    print("CMD_LIST when waiting result:", CMD_LIST)
    TIMER = threading.Timer(5, _remove_cmd_from_list)
    TIMER.start()
    # _send_cmd()
    
    
    
    
def recieve_cmd_result():    #for UI
    global CMD_LIST
    global TIMER
    while CMD_LIST:

        if CMD_LIST[0].cmd_response_obj:
            result = CMD_LIST[0]
            CMD_LIST.pop(0)
            print("CMD_LIST after success return:", CMD_LIST)
            TIMER.cancel()
            return result
            
        

def dat_data():  #upload dat data to UI
    global DAT_LIST
    while DAT_LIST:
        dat_data = DAT_LIST[0]
        print(dat_data)
        DAT_LIST.pop(0)

def initial():
    ###initial:tell parser frame where to put output
    parser_frame.regist_call_back(_recieve_cmd, _recieve_dat)


def reset():    # for UI
    global CMD_LIST
    global DAT_LIST
    global TIMER
    CMD_LIST = []
    DAT_LIST = []
    TIMER = None
        
def _send_cmd():
    global CMD_LIST
    
    # TIMER = threading.Timer(5, remove_cmd_from_list)
    # TIMER.start()
    while len(CMD_LIST) != 0:
        #send CMD_LIST[0].type_key
        pass




# tell paser frame where to imput'''
def _recieve_dat(dat_response):
    global DAT_LIST
    print("in_dat")
    print(dat_response)
    DAT_LIST.append(dat_response)
    print("after append")
    print(DAT_LIST)

def _recieve_cmd(cmd_response):
    global CMD_LIST 
    print("in recieve")
    
    try:

        # if error occur, put error to CMD_LIST[0].cmd_response_obj
        if cmd_response == parser_frame.ERROR_STRING_TYPE1 or \
           cmd_response == parser_frame.ERROR_STRING_TYPE2 or \
           cmd_response == parser_frame.ERROR_STRING_TYPE3:
           CMD_LIST[0].cmd_response_obj = cmd_response
           

        elif cmd_response.type_key in CMD_LIST[0].type_key:
            CMD_LIST[0].cmd_response_obj = cmd_response

        else:
            print("Wrong result")
            
    except IndexError:
        print("NO command waiting for response!!")
        
        
                
def _remove_cmd_from_list():
    global CMD_LIST 
    del CMD_LIST[0]
    print("Out of time!!!!")
    print("CMD_LIST after time out:", CMD_LIST)
    if CMD_LIST:
        _send_cmd()





#!!!!   if lost some data in the trasform process, it will crash 
data = b'CLI=get fntents:nnnnnnnn ssss eeee,le+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n+DAT:\x05\x00\x01\x00\x02\x00\x00\r\n+DAT:\x05\x00\x01\x00\x03\x00\x00\r\n+DAT:\x05\x00\x01\x00\x04\x00\x00\r\n+DAT:\x05\x00\x01\x00\x05\x00\x00\r\n+DAT:\x05\x00\x01\x00\x06\x00\x00\r\n+DAT:\x05\x00\x01\x00\x07\x00\x00\r\n+DAT:\x05\x00\x01\x00\x08\x00\x00\r\n+DAT:\x05\x00\x01\x00\t\x00\x00\r\n+DAT:\x05\x00\x01\x00\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x0b\x00\x00\r\n'
data1 = b"CLI=get file_contents:nnnnnnnn,ssss,ee"

data_dat = b"+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n+DAT:\x05\x00\x01\x00\x02\x00\x00\r\n+DAT:\x05\x00\x01\x00\x03\x00\x00\r\n+DAT:\x05\x00\x01\x00\x04\x00\x00\r\n+DAT:\x05\x00\x01\x00\x05\x00\x00\r\n+DAT:\x05\x00\x01\x00\x06\x00\x00\r\n+DAT:\x05\x00\x01\x00\x07\x00\x00\r\n+DAT:\x05\x00\x01\x00\x08\x00\x00\r\n+DAT:\x05\x00\x01\x00\t\x00\x00\r\n+DAT:\x05\x00\x01\x00\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x0b\x00\x00\r\n"
data2 = b"CLI=get file_size:6543,23\r\n"
data3 = b"CLI=rm file:HR_20170210133100.dat,34\r\n"
error_data = b"Command parameter error\r\n"
data4 = b"CLI=get dat_char:3,4,21\r\n"
data5 = b"CLI=get dat_char:999,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,1,180,70,25,79\r\n"
data6 = b"CLI=start dat:0020,250,24,2400,6.000000,0.000000,1,51\r\n+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n"
data7 = b"CLI=get range:1 250,19\r\n"
data8 = b"CLI=start calib:Acc calibration pass,37\r\n"



cmd1 = b"SYS get file_contents nnnnnnnn ssss eeee\r\n"
cmd2 = b"SYS get file_size HR_201702101143100.dat\r\n"
cmd3 = b"SYS rm file HR_20170210133100.dat\r\n"
cmd4 = b"SYS get dat_char 3\r\n"
cmd5 = b"SYS get dat_char 999\r\n"
cmd6 = b"SYS start dat 0020\r\n"
cmd7 = b"SYS get range 1\r\n"
cmd8 = b"SYS start calib 1\r\n"



initial()

###send command       put command obj in CMD LIST
store_cmd(cmd6)

#Assume the return data
parser_frame.recieve_data_to_buffer(data_dat)

obj = recieve_cmd_result()
dat_data()
print(DAT_LIST)
try:
    
    print("position of pass_return obj:", obj.cmd_response_obj)
    print("lenth of pass reutrn:", obj.cmd_response_obj.len)
    
    

except AttributeError:
    print("No valid data return")







        





