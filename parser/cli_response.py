

class CliResponseParser():
    def __init__(self):
        self.type_int = None
        self.cmd = None
        self.parameters = None    
        self.type_key = None
            
           
    def mapping_parser(self, cmd, parameters, parser_type):
        parser_object =cmd_response_parsers.create_parser(parser_type)
        
        parser_object.attribute_parser(parameters, cmd)
        return parser_object       

    def cli_cmd(self, input_repsonse):
        
        self.cmd, self.parameters = input_repsonse.split(b":", 1)
        self.type_key = self.cmd.split(b"=")[1]        
        self.type_int = parser_type.CMD_STRING_MAP.get(self.type_key)

    def create_cmd_parser(self, input_repsonse):
        self.cli_cmd(input_repsonse)
        return self.mapping_parser(self.cmd, self.parameters, self.type_int)



# with open("D:\Python\\dat_000c.txt", "rb") as f:
#     content = f.read()
#     print(content)
# content = b"CLI=start dat:077f,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,65\r\n+DAT:\x14\x00S\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00r\x01\x00\xff\r\n" 
# cli = CliResponseParser()
# send_data_obj = cli.create_cmd_parser(content)
# data_parser_obj = send_data_obj.create_dat_parser()
print(float(b'6.000000'))
# print(cli.parameters)

# print(send_data_obj.dat_data)


# print("HRB:", data_parser_obj.hrb)
# print("RRIB", data_parser_obj.rrib)
# print("Acc:",data_parser_obj.acc)
# print("Gyr:",data_parser_obj.gyr)
# print("ECG:", data_parser_obj.ecg_raw_data)
# print("CNTB:", data_parser_obj.cntb)
# print("RSCB:", data_parser_obj.rscb)
# print("RESB:", data_parser_obj.resb)
# print("TEM:", data_parser_obj.temperature)
# print("POST:", data_parser_obj.posture)
# print("AF:", data_parser_obj.af)
# get_sysobj = cli.create_parser("CLI=get status:MAC=xx.xx.xx.xx.xx.xx,Project_Name=nnnnnn,CLI_Version=Vc,Boot_Version=Vb.b.b,HW_Version=Vh.h.h,FW_Version=Vf.f.f,CLOCK=YYYYMMDDhhmmss,Storage_Capacity=tttttt,Last_Capacity=rrrrrr,len")
# set_sysobj = cli.create_parser("CLI=set reset:x,len")
# rtc_object = cli.create_parser("CLI=set RTC:YYYYMMDDhhmmss,len")
# utc_object = cli.create_parser("CLI=set UTC:YYYYMMDhhmmss,TimeZone,len")
# rsoc_object = cli.create_parser("CLI=get SOC:x,len")
# mfg_object = cli.create_parser("CLI=set MFG:x pppppppp,len")
# get_counter_object = cli.create_parser("CLI=get ResetCounter:ccc,len")
# set_counter_object = cli.create_parser("CLI=set ResetCounter:ccc,len")
# boot_mode_object = cli.create_parser("CLI=set boot:password,len")
# project_mode_object = cli.create_parser("CLI=set mode:mode,len")
# information_object = cli.create_parser("CLI=set pi:gender height weight age,len")
# file_list_object = cli.create_parser("CLI=get file_list:nnnnnnnn,...,nnnnnnnn,len")
# file_size_object = cli.create_parser("CLI=get file_size:ssss,len")
# file_contents_object = cli.create_parser("CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n[data 1][data 2]…[data N][Checksum]")
# file_remove_object = cli.create_parser("CLI=rm file:nnnnnnnn,len")
# test_file_object = cli.create_parser("CLI=file_test:nnn,sss,ccc,len")
# binary_object = cli.create_parser("CLI=get dat_char:999,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,1,180,70,25,79")
# binary_object = cli.create_parser("CLI=get dat_char:998,077F,26")
# binary_object = cli.create_parser("CLI=get dat_char:3,4,21")
# stop_send_binary_object = cli.create_parser("CLI=stop dat:len")
# stop_send_cmp_object = cli.create_parser("CLI=stop dat_cmp:len")
# set_ecg_package_object = cli.create_parser("CLI=set dat_eps:size,len")
# get_ecg_package_object = cli.create_parser(content)
# calbri_acc_object = cli.create_parser("CLI=start calib:sel,len")
# montion_datarate_object = cli.create_parser("CLI=set odr:rate,len")
# get_sensor_range_object = cli.create_parser("CLI=get range:x rang,len")

# set_sensor_range_object = cli.create_parser("CLI=set range:x rang,len")

# send_binary_object = cli.create_parser(content)
    
# #     print(set_sensor_range_object.cmd)
# #     print(cli.type)
# #     print(cli.parameters)
   
# # except Exception as msg:
# #     print("false")
# #     print(msg)





# print("_"*50)
# print("get_sysobj type:", type(get_sysobj), "get_sysobj name:", get_sysobj.cmd, "\nmac:", get_sysobj.mac, "\nProject_Name:", get_sysobj.project_name)
# print("_"*50)
# print("rtc_obj type:",type(rtc_object), "\nrtc_date:", rtc_object.date)
# print("_"*50)
# print("utc_obj type:",type(utc_object), "\nutc_date:", utc_object.date)
# print("_"*50)
# print("rsoc_obj type:", type(rsoc_object), "\nrsoc_rsoc:", rsoc_object.rsoc)
# print("_"*50)
# print("mfg_obj type:", type(mfg_object), "\nmfg_password:", mfg_object.password)
# print("_"*50)
# print("counter_obj type:", type(get_counter_object), "\nget counter value:", get_counter_object.counter_value)
# print("_"*50)
# print("counter_obj type:", type(set_counter_object), "\nset counter value:", set_counter_object.set_counter_value)
# print("_"*50)
# print("boot_mode_obj type:", type(boot_mode_object), "\nbood_mode password:", boot_mode_object.password)
# print("_"*50)
# print("project_mode_obj type:", type(project_mode_object), "\nproject_mode:", project_mode_object.mode)
# print("_"*50)
# print("information_obj type:", type(information_object), "\ngender:", information_object.gender, "\nheight:", information_object.height)
# print("_"*50)
# print("get_filelist_obj type:", type(file_list_object), "\nfile_list:", file_list_object.list_array)
# print("_"*50)
# print("get_filesize_obj type:", type(file_size_object), "\nfile_size:", file_size_object.file_size)
# print("_"*50)
# print("get_filecontents_obj type:", type(file_contents_object), "\nfile_name:", file_contents_object.file_name, "\nfile_contents:", file_contents_object.file_content)
# print("_"*50)
# print("file_remove_obj type:", type(file_remove_object), "\nfile_name:", file_remove_object.file_name)
# print("_"*50)
# print("file_test_obj type:", type(test_file_object), "\nfile_name:", test_file_object.file_name)
# print("_"*50)
# print("binary_obj type:", type(binary_object), "\nsupport_dict:", binary_object.support_dic)
# print("binary_obj type:", type(binary_object), "\nval:", binary_object.val)
# print("_"*50)
# print("stop_send_dat_obj type:", type(stop_send_binary_object), "\nlen:", stop_send_binary_object.len)
# print("_"*50)
# print("stop_send_cmp_obj type:", type(stop_send_cmp_object), "\nlen:", stop_send_cmp_object.len)
# print("_"*50)
# print("set_ecg_package_obj type:", type(set_ecg_package_object), "\nsize:", set_ecg_package_object.size)
# print("_"*50)
# print("get_ecg_package_obj type:", type(get_ecg_package_object), "\nsize:", get_ecg_package_object.size)
# print("_"*50)
# print("calbri_acc_obj type:", type(calbri_acc_object), "\nsel:", calbri_acc_object.sel)
# print("_"*50)
# print("montion_datarate_obj type:", type(montion_datarate_object), "\nrate:", montion_datarate_object.rate)
# print("_"*50)
# print("get_sensor_range_obj type:", type(get_sensor_range_object), "\nrange:", get_sensor_range_object.range)
# print("_"*50)
# print("set_sensor_range_obj type:", type(set_sensor_range_object), "\nrange:", set_sensor_range_object.range)
# print("_"*50)

