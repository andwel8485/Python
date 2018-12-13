import cmd_response_parsers
import dat_parser


cli_fac = cmd_response_parsers.CliResponseParser()
dat_fac = dat_parser.DatParser()

CR_LN = b"\r\n"
DAT_STRING = b"+DAT:"
CLI_STRING = b"CLI="
LEN_LEN = 2

ERROR_STRING_TYPE1 = b"Command is not found\r\n"
ERROR_STRING_TYPE2 = b"Invalid Parameter\r\n"
ERROR_STRING_TYPE3 = b"Command parameter error\r\n"

CMD_FUNC = None
DAT_FUNC = None

RESPONSE_COMPLETE = 3
RESPONSE_WRONG_LENTH = 2
RESPONSE_INCOMPLETE = 1

BUFFER = b""
COMPLETE_RESPONSE = []


def _first_find_dat_in_buffer(dat_index):
    global BUFFER
    global COMPLETE_RESPONSE
    print("in first find dat")

    start_index = dat_index
    binary_index = start_index + len(DAT_STRING)
    dat_len = int.from_bytes(BUFFER[binary_index : (binary_index + LEN_LEN)], byteorder="little")    #!!!!!!!
    end_index = binary_index + dat_len + len(CR_LN) + LEN_LEN
    dat_complete_parser = BUFFER[start_index:end_index]
    if len(dat_complete_parser) < dat_len + len(DAT_STRING) + len(CR_LN) + LEN_LEN:
        return RESPONSE_INCOMPLETE
    if dat_complete_parser[-2:] != CR_LN:
        # print("clean BUFFER")
        BUFFER = BUFFER[binary_index:]
        return RESPONSE_WRONG_LENTH
        
    # print("BUFFER fine")
    BUFFER = BUFFER[end_index:]
    # print("BUFFER:", BUFFER)
    
    # print("dat:",dat_complete_parser)
    dat_obj = dat_fac.distrubute_dat_data(dat_complete_parser)
    COMPLETE_RESPONSE.append(dat_obj)
    print(type(dat_obj))
    return RESPONSE_COMPLETE

def _first_find_cmd_in_buffer(cmd_index):
    global BUFFER
    global COMPLETE_RESPONSE
    
    start_index = cmd_index
    BUFFER = BUFFER[start_index:]
    end_index = BUFFER.find(CR_LN)
    if end_index == -1:  
        print("fail")
        return RESPONSE_INCOMPLETE   
    cmd_complete_parser = BUFFER[start_index:end_index]

    #check if cmd_complete parser has missing dat between "CLI=" and "\r\n"
    len_of_cmd_complete_parser = cmd_complete_parser.rsplit(b",", 1)[1]
    try:
        #comma lenth = 1
        if len(cmd_complete_parser.rsplit(b",", 1)[0]) + 1 != int(len_of_cmd_complete_parser):
            print("cmd_lenth_error")
            print(len(cmd_complete_parser.rsplit(b",", 1)[0]))
            print(int(len_of_cmd_complete_parser))
            BUFFER = BUFFER[(end_index + len(CR_LN)):]
            return RESPONSE_WRONG_LENTH
    except ValueError:
        print("value fail")
        BUFFER = BUFFER[(end_index + len(CR_LN)):]
        print(BUFFER)
        return RESPONSE_WRONG_LENTH

    cli_obj = cli_fac.create_cmd_parser(cmd_complete_parser)
    COMPLETE_RESPONSE.append(cli_obj)
    if cli_fac.type_int == 21:
        dat_fac.setting_parameters(cli_obj)

    print("before buffer clean:", BUFFER)
    print("end index:", end_index)
    print("after process")
    BUFFER = BUFFER[end_index:]
    print("buffer:", BUFFER)
    return RESPONSE_COMPLETE

def upload(complete_response_list):
    complete_response = complete_response_list[0]
    complete_response_list.pop(0)
    return complete_response

    

def _find_error_in_buffer(error_index):
    global BUFFER

    start_index = error_index
    BUFFER = BUFFER[start_index:]
    end_index = BUFFER.find(CR_LN) + len(CR_LN)
    error_complete_data = BUFFER[start_index: end_index]
    BUFFER = BUFFER[end_index:]
    return error_complete_data

def _find_min(data_list):
    index_list = sorted(data_list)
    for value in index_list:
        if value  >= 0: 
            return value
    return -1
    
    
def check_buffer(buffer):
    global BUFFER
    global COMPLETE_RESPONSE
    print("BUFFER before loop:", BUFFER)
 
    while BUFFER != b"":
        print("In check buffer")
        
        # print("global:", BUFFER)
        dat_index = BUFFER.find(DAT_STRING)
        cmd_index = BUFFER.find(CLI_STRING)
        error_index = _find_min([BUFFER.find(ERROR_STRING_TYPE1), \
                                 BUFFER.find(ERROR_STRING_TYPE2), \
                                 BUFFER.find(ERROR_STRING_TYPE3)])

        startdata = _find_min([dat_index, cmd_index, error_index])

        if startdata == -1:
            break
        
        elif startdata == dat_index:
            result = _first_find_dat_in_buffer(dat_index)
            if result == RESPONSE_INCOMPLETE:
                break
            elif result == RESPONSE_WRONG_LENTH:
                continue
            elif result == RESPONSE_COMPLETE:
                upload_complete_dat(upload(COMPLETE_RESPONSE))

        elif startdata == cmd_index:
            result = _first_find_cmd_in_buffer(cmd_index)
            if result == RESPONSE_INCOMPLETE:
                print("not enougj lenth ")
                break
            elif result == RESPONSE_WRONG_LENTH:
                print("continue")
                continue
            elif result == RESPONSE_COMPLETE:
                print("success return obj")
                upload_complete_cmd(upload(COMPLETE_RESPONSE))  

        elif startdata == error_index:
            print("find error_index")
            error_messege = _find_error_in_buffer(error_index)
            upload_complete_cmd(error_messege)
            continue




        # print(error_index)
        # print(dat_index)
        # print(cmd_index)

        # if (dat_index == -1) and (cmd_index == -1) and (error_index == -1):
        #     break
        
        # elif (dat_index > -1) and (cmd_index == -1) and (error_index == -1):
        #     print("only DAT")
        #     result = _first_find_dat_in_buffer(dat_index)
        #     if result == RESPONSE_INCOMPLETE:
        #         break
        #     elif result == RESPONSE_WRONG_LENTH:
        #         continue
        #     elif result == RESPONSE_COMPLETE:
        #         upload_complete_dat(upload(COMPLETE_RESPONSE))

        # elif (dat_index == -1) and (cmd_index > -1) and (error_index == -1):
        #     print("only CMD ")
        #     obj = _first_find_cmd_in_buffer(cmd_index)
        #     if obj == RESPONSE_INCOMPLETE:
        #         print("not enougj lenth ")
        #         break
        #     elif obj == RESPONSE_WRONG_LENTH:
        #         print("continue")
        #         continue
        #     elif obj == RESPONSE_COMPLETE:
        #         print("success return obj")
        #         upload_complete_cmd(upload(COMPLETE_RESPONSE))  

        # elif (dat_index == -1) and (cmd_index == -1) and (error_index > -1):
        #     error_messege = _find_error_in_buffer(error_index)
        #     upload_complete_cmd(error_messege)
            
        # elif (dat_index > -1) and (cmd_index > -1) and (error_index == -1):
        #     print("DAT&CMD")
        #     if dat_index < cmd_index:
        #         print("DAT first")
        #         obj = _first_find_dat_in_buffer(dat_index)
        #         if obj:
        #             upload_complete_dat(obj)
        #         else:
        #             break
        #     else:
        #         print("CMD first")
        #         obj = _first_find_cmd_in_buffer(cmd_index)
        #         print(obj)
        #         if obj == RESPONSE_INCOMPLETE:
        #             print("not enougj lenth")
        #             break
        #         elif obj == RESPONSE_WRONG_LENTH:
        #             print("continue")
        #             continue
        #         elif obj == RESPONSE_COMPLETE:
        #             print("success return obj")
        #             upload_complete_cmd(upload(COMPLETE_RESPONSE))

        # elif (dat_index > -1) and (cmd_index == -1) and (error_index > -1):
        #     if dat_index < error_index:
        #         obj = _first_find_dat_in_buffer(dat_index)
        #         if obj:
        #             upload_complete_dat(obj)
        #         else:
        #             break
        #     else:
        #         error_messege = _find_error_in_buffer(error_index)
        #         upload_complete_cmd(error_messege)

        # elif (dat_index == -1) and (cmd_index > -1) and (error_index > -1):
        #     if cmd_index < error_index:
        #         obj = _first_find_cmd_in_buffer(cmd_index)

        #         if obj == RESPONSE_INCOMPLETE:
        #             print("not enougj lenth ")
        #             break
        #         elif obj == RESPONSE_WRONG_LENTH:
        #             print("continue")
        #             continue
        #         elif obj == RESPONSE_COMPLETE:
        #             print("success return obj")
        #             upload_complete_cmd(upload(COMPLETE_RESPONSE))
        #     else:
        #         error_messege = _find_error_in_buffer(error_index)
        #         upload_complete_cmd(error_messege)

        # elif (dat_index > -1) and (cmd_index > -1) and (error_index > -1):
        #     if min(dat_index, cmd_index, error_index) == dat_index:
        #         obj = _first_find_dat_in_buffer(dat_index)
        #         if obj:
        #             upload_complete_dat(obj)
        #         else:
        #             break
        #     elif min(dat_index, cmd_index, error_index) == cmd_index:
        #         obj = _first_find_cmd_in_buffer(cmd_index)

        #         if obj == RESPONSE_INCOMPLETE:
        #             print("not enougj lenth ")
        #             break
        #         elif obj == RESPONSE_WRONG_LENTH:
        #             print("continue")
        #             continue
        #         elif obj == RESPONSE_COMPLETE:
        #             print("success return obj")
        #             upload_complete_cmd(upload(COMPLETE_RESPONSE))
                
        #     elif min(dat_index, cmd_index, error_index) == error_index:
        #         error_messege = _find_error_in_buffer(error_index)
        #         upload_complete_cmd(error_messege)
   
    
def recieve_data_to_buffer(data):
    global BUFFER 
    
    # print("dat", data)
    BUFFER += data
    check_buffer(BUFFER)
    # except:
    #     print("worng")

def upload_complete_cmd(obj):  
    print("In parser frame upload_complete_cmd func")
    print("Type of upload object:", type(obj))
    # print(obj)
    # print(BUFFER)
    CMD_FUNC(obj)

def upload_complete_dat(obj):
    # print("upload DAT")
    # print(obj)
    DAT_FUNC(obj)
    
def regist_call_back(cmd_func, dat_func):
    global CMD_FUNC
    global DAT_FUNC
    print("regist")
    CMD_FUNC = cmd_func
    DAT_FUNC = dat_func



def refresh_buffer():
    global BUFFER
    BUFFER = b""

if __name__ == "__main__":
    # data1 = b'+DAT:\x05\x00'
    cmd = b"CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n"
    data6 = b"CLI=start dat:0020,250,24,2400,6.000000,0.000000,1,51\r\n+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n"
    # cmd_dat = b""
    # data2 = b"+DAT:\x9a\x00\x04\x00\x00\x04\xfe\xe6\x05B\x11\x87\xfd\xc5\x05k\x11\xb0\xfd\x8e\x05\xd5\x11\x8c\xfd\xc0\x05\xba\x11\xc8\xfdq\x06\x7f\x11\x91\xfd\x1c\x06y\x11~\xfd\xe5\x052\x11d\xfd\xc4\x05\x9a\x11\xe1\xfd\x04\x06\xcd\x11\x98\xfd\xf2\x05g\x11\xe6\xfd\x10\x06\x8d\x11p\xfd\xa3\x05i\x11\x8a\xfd\x9d\x05\xa7\x11\xd7\xfd\xd5\x05\xa5\x11\xed\xfdj\x06\xaf\x11\x9c\xfd\xc6\x05F\x118\xfd\x89\x05\x95\x11\x96\xfd\xdb\x05\x87\x11\xb8\xfd\xfc\x05Y\x11\xed\xfd\xf5\x05\x9a\x11\xa5\xfd\xce\x058\x11\xce\xfd\xa4\x05*\x11\xd7\xfd\xf6\x05\xb9\x11\x96\xfd\xb1\x05m\x11\xe5\xfd\x06\x06\xa8\x11\r\n"
    data = b'CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n+DAT:\x05\x00\x01\x00\x02\x00\x00\r\n+DAT:\x05\x00\x01\x00\x03\x00\x00\r\n+DAT:\x05\x00\x01\x00\x04\x00\x00\r\n+DAT:\x05\x00\x01\x00\x05\x00\x00\r\n+DAT:\x05\x00\x01\x00\x06\x00\x00\r\n+DAT:\x05\x00\x01\x00\x07\x00\x00\r\n+DAT:\x05\x00\x01\x00\x08\x00\x00\r\n+DAT:\x05\x00\x01\x00\t\x00\x00\r\n+DAT:\x05\x00\x01\x00\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x0b\x00\x00\r\n'
    recieve_data_to_buffer(data6)
    