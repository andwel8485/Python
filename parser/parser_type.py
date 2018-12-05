


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
    GET_FILE_LIST = 14
    GET_FILE_SIZE = 15
    GET_FILE_CONTENTS = 16
    REMOVE = 17
    FILE_TEST = 18
    GET_DAT_CHAR = 19
    STOP_DAT = 20
    STOP_DAT_CMP = 21
    SET_DAT_EPS = 22
    GET_DAT_EPS = 23
    START_CALIB = 24
    SET_ODR = 25 
    GET_RANGE = 26 
    SET_RANGE = 27
    START_DAT = 28
    

CMD_STRING_MAP = {
    "get status": CmdType.GET_STATUS,
    "set reset": CmdType.SET_RESET,
    "set RTC": CmdType.SET_RTC,
    "get RTC": CmdType.GET_RTC,
    "set UTC": CmdType.SET_UTC,
    "get UTC": CmdType.GET_UTC,
    "get SOC": CmdType.GET_SOC,
    "set MFG": CmdType.SET_MFG,
    "get ResetCounter": CmdType.GET_RESETCOUNTER,
    "set ResetCounter": CmdType.SET_RESETCOUNTER,
    "set boot": CmdType.SET_BOOT,
    "set mode": CmdType.SET_MODE,
    "set pi": CmdType.SET_PI,
    "get file_list": CmdType.GET_FILE_LIST,
    "get file_size": CmdType.GET_FILE_SIZE, 
    "get file_contents": CmdType.GET_FILE_CONTENTS,
    "rm file": CmdType.REMOVE, 
    "file_test": CmdType.FILE_TEST,
    "get dat_char": CmdType.GET_DAT_CHAR,
    "stop dat":  CmdType.STOP_DAT, 
    "stop dat_cmp": CmdType.STOP_DAT_CMP,
    "set dat_eps": CmdType.SET_DAT_EPS, 
    "get dat_eps": CmdType.GET_DAT_EPS, 
    "start calib": CmdType.START_CALIB,
    "set odr": CmdType.SET_ODR,
    "get range": CmdType.GET_RANGE, 
    "set range": CmdType.SET_RANGE,
    b"start dat": CmdType.START_DAT
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

