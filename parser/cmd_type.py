


class CmdType():
    GET_STATUS = 1
    SET_RESET = 2  
    SET_RTC = 3
    GET_RTC = 4
    SET_UTC = 5
    GET_UTC = 6
    GET_SOC = 7
    SET_MFG = 8
    GET_RESETCOUNTER = 9
    SET_RESETCOUNTER = 10
    SET_BOOT = 11
    SET_MODE = 12
    SET_PI = 13
    GET_PI = 14
    GET_FILE_LIST = 15
    GET_FILE_SIZE = 16
    GET_FILE_CONTENTS = 17
    REMOVE = 18
    FILE_TEST = 19
    GET_DAT_CHAR = 20
    START_DAT = 21
    STOP_DAT = 22
    START_DAT_CMP = 23
    STOP_DAT_CMP = 24
    SET_DAT_EPS = 25
    GET_DAT_EPS = 26
    START_CALIB = 27
    SET_ODR = 28
    GET_RANGE = 29
    SET_RANGE = 30
    
    

CMD_STRING_MAP = {
    b"get status": CmdType.GET_STATUS,
    b"set reset": CmdType.SET_RESET,
    b"set RTC": CmdType.SET_RTC,
    b"get RTC": CmdType.GET_RTC,
    b"set UTC": CmdType.SET_UTC,
    b"get UTC": CmdType.GET_UTC,
    b"get SOC": CmdType.GET_SOC,
    b"set MFG": CmdType.SET_MFG,
    b"get ResetCounter": CmdType.GET_RESETCOUNTER,
    b"set ResetCounter": CmdType.SET_RESETCOUNTER,
    b"set boot": CmdType.SET_BOOT,
    b"set mode": CmdType.SET_MODE,
    b"set pi": CmdType.SET_PI,
    b"get pi": CmdType.GET_PI,
    b"get file_list": CmdType.GET_FILE_LIST,
    b"get file_size": CmdType.GET_FILE_SIZE, 
    b"get file_contents": CmdType.GET_FILE_CONTENTS,
    b"rm file": CmdType.REMOVE, 
    b"file_test": CmdType.FILE_TEST,
    b"get dat_char": CmdType.GET_DAT_CHAR,
    b"start dat": CmdType.START_DAT,
    b"stop dat": CmdType.STOP_DAT, 
    b"start dad_cmp": CmdType.START_DAT_CMP,
    b"stop dat_cmp": CmdType.STOP_DAT_CMP,
    b"set dat_eps": CmdType.SET_DAT_EPS, 
    b"get dat_eps": CmdType.GET_DAT_EPS, 
    b"start calib": CmdType.START_CALIB,
    b"set odr": CmdType.SET_ODR,
    b"get range": CmdType.GET_RANGE, 
    b"set range": CmdType.SET_RANGE,
    
}

# cli = "set range"
# cmd_type = CMD_STRING_MAP.get(cli)
# print(cmd_type)
# command = Enum("get status", "CLI=set reset", "CLI=set RTC", "CLI=get RTC", "CLI=set UTC", \
#                "CLI=get UTC", "CLI=get SOC", "CLI= set MFG", "CLI= get ResetCounter", "CLI= set ResetCounter", \
#                "CLI=set boot", "CLI=set mode", "CLI= set pi", "CLI=get file_list", "CLI=get file_size", \
#                "CLI=get file_contents", "CLI=rm file", "CLI=file_test", "CLI=get dat_char", "CLI=stop dat", \
#                "CLI=stop dat_cmp", "CLI=set dat_eps", "CLI=get dat_eps", "CLI=start calib", "CLI=set odr", \
#                "CLI=get range", "CLI=set range")

