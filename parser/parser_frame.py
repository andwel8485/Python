import cmd_response_parsers
import dat_parser

cli_fac = cmd_response_parsers.CliResponseParser()
dat_fac = dat_parser.DatParser()

BUFFER = b""


def _first_find_dat_in_buffer():
    global BUFFER

    start_index = BUFFER.find(b"+DAT:")
    binary_index = start_index + 5
    dat_len = int.from_bytes(BUFFER[binary_index : (binary_index + 2)], byteorder="little")
    end_index = binary_index + dat_len + 4
    dat_complete_parser = BUFFER[start_index:end_index]
    if len(dat_complete_parser) < dat_len + 9:
        return False
    if dat_complete_parser[-2:] != b"\r\n":
        print("clean BUFFER")
        BUFFER = BUFFER[binary_index:]
        
    print("BUFFER fine")
    BUFFER = BUFFER[end_index:]
    print("BUFFER:", BUFFER)
    dat_fac.distrubute_dat_data(dat_complete_parser)
    print("dat:",dat_complete_parser)
    return True

def _first_find_cmd_in_buffer():
    global BUFFER
    
    start_index = BUFFER.find(b"CLI=")
    end_index = BUFFER.find(b"\r\n") + 2
    if end_index > start_index:
        print("end>start -- good")
        cmd_complete_parser = BUFFER[start_index:end_index]
        cli_fac.create_cmd_parser(cmd_complete_parser)
        if cli_fac.type_int == 21:
            dat_fac.setting_parameters(cli_fac.create_cmd_parser(cmd_complete_parser))
        print("cmd:",cmd_complete_parser)
        BUFFER = BUFFER[end_index:]
        return True
    else:
        print("end<start -- bad")
        print("clean BUFFER")
        BUFFER = BUFFER[start_index:]
        end_index = BUFFER.find(b"\r\n") + 2
        if end_index == -1:
            return False
        cmd_complete_parser = BUFFER[:end_index]
        cli_fac.create_cmd_parser(cmd_complete_parser)
        BUFFER = BUFFER[end_index:]
        print("cmd:", cmd_complete_parser)
        return True


def _check_buffer(buffer):
    global BUFFER

    
    while BUFFER != b"":
        print("global:", BUFFER)
        dat_index = BUFFER.find(b"+DAT:")
        cmd_index = BUFFER.find(b"CLI=")

    
        if dat_index != -1 and cmd_index == -1:
            print("dat first")  
            if not _first_find_dat_in_buffer():
                break          
        
        elif (dat_index == -1) and (cmd_index != -1):
            
            print("cmd first")
            if not _first_find_cmd_in_buffer():
                break  
            
        elif cmd_index < dat_index:        
            print("cmd first")
            if not _first_find_cmd_in_buffer():
                break
                
        elif cmd_index > dat_index:
            print("dat first")  
            if not _first_find_dat_in_buffer():
                break
        elif b"SMP_ERROR_NOT_FOUND: Command is not found\r\n" in BUFFER:
             
            cmd_complete_parser = b"SMP_ERROR_NOT_FOUND: Command is not found\r\n"
            BUFFER = b"".join(BUFFER.split(b"SMP_ERROR_NOT_FOUND: Command is not found\r\n"))
        elif b"SMP_ERROR_INVALID_PARAMETER: Invalid Parameter\r\n" in BUFFER:
            cmd_complete_parser = b"SMP_ERROR_INVALID_PARAMETER: Invalid Parameter\r\n"
            BUFFER = b"".join(BUFFER.split(b"SMP_ERROR_INVALID_PARAMETER: Invalid Parameter\r\n"))

        elif b"SMP_ERROR_DISCRIMINATION: Command parameter error" in BUFFER:
            start_index = BUFFER.find(b"SMP_ERROR_DISCRIMINATION: Command parameter error")
            end_index = BUFFER.find(b"\r\n")
            if end_index > start_index:
                cmd_complete_parser = BUFFER[start_index:(end_index + 2)]
                BUFFER = BUFFER[(end_index + 2):]
            elif end_index < start_index:
                BUFFER = BUFFER[start_index:]
                end_index = BUFFER.find(b"\r\n")
                if end_index == -1:
                    return False
                cmd_complete_parser = BUFFER[:(end_index + 2)]
                BUFFER = BUFFER[(end_index + 2):]
                return True
        else:
            return 
        
    
         


def recieve_data_to_buffer(data):
    global BUFFER
    
    BUFFER += data
    _check_buffer(BUFFER)


def refresh_buffer():
    global BUFFER
    BUFFER = b""


data1 = b'+DAT:\x05\x00'
cmd = b"CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n"
cmd_dat = b""
data2 = b"+DAT:\x9a\x00\x04\x00\x00\x04\xfe\xe6\x05B\x11\x87\xfd\xc5\x05k\x11\xb0\xfd\x8e\x05\xd5\x11\x8c\xfd\xc0\x05\xba\x11\xc8\xfdq\x06\x7f\x11\x91\xfd\x1c\x06y\x11~\xfd\xe5\x052\x11d\xfd\xc4\x05\x9a\x11\xe1\xfd\x04\x06\xcd\x11\x98\xfd\xf2\x05g\x11\xe6\xfd\x10\x06\x8d\x11p\xfd\xa3\x05i\x11\x8a\xfd\x9d\x05\xa7\x11\xd7\xfd\xd5\x05\xa5\x11\xed\xfdj\x06\xaf\x11\x9c\xfd\xc6\x05F\x118\xfd\x89\x05\x95\x11\x96\xfd\xdb\x05\x87\x11\xb8\xfd\xfc\x05Y\x11\xed\xfd\xf5\x05\x9a\x11\xa5\xfd\xce\x058\x11\xce\xfd\xa4\x05*\x11\xd7\xfd\xf6\x05\xb9\x11\x96\xfd\xb1\x05m\x11\xe5\xfd\x06\x06\xa8\x11\r\n"
data = b'CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n+DAT:\x05\x00\x01\r\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x01\x00\x00\r\n+DAT:\x05\x00\x01\x00\x02\x00\x00\r\n+DAT:\x05\x00\x01\x00\x03\x00\x00\r\n+DAT:\x05\x00\x01\x00\x04\x00\x00\r\n+DAT:\x05\x00\x01\x00\x05\x00\x00\r\n+DAT:\x05\x00\x01\x00\x06\x00\x00\r\n+DAT:\x05\x00\x01\x00\x07\x00\x00\r\n+DAT:\x05\x00\x01\x00\x08\x00\x00\r\n+DAT:\x05\x00\x01\x00\t\x00\x00\r\n+DAT:\x05\x00\x01\x00\n\x00\x00\r\n+DAT:\x05\x00\x01\x00\x0b\x00\x00\r\n'
recieve_data_to_buffer(data)
