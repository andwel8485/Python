import parser_class
import parser_type

class CliResponseParser():
    def __init__(self):
        self.type = None
        self.cmd = None
        self.parameters = None    
        self.type_key = None    
           
    def mapping_parser(self, cmd, parameters, parser_type):
        parser_object = parser_class.create_parser(parser_type)
        
        parser_object.attribute_parser(parameters, cmd)
        return parser_object       

    def cli_cmd(self, input_repsonse):
        
        cmd_list = input_repsonse.split(":")
        self.cmd = cmd_list[0]
        self.type_key = self.cmd.split("=")[1]
        self.parameters = cmd_list[1]   
        self.type = parser_type.CMD_STRING_MAP.get(self.type_key)
        

    def create_parser(self, input_repsonse):
        self.cli_cmd(input_repsonse)
        return self.mapping_parser(self.cmd, self.parameters, self.type)


cli = CliResponseParser()
get_sysobj = cli.create_parser("CLI=get status:MAC=xx.xx.xx.xx.xx.xx,Project_Name=nnnnnn,CLI_Version=Vc,Boot_Version=Vb.b.b,HW_Version=Vh.h.h,FW_Version=Vf.f.f,CLOCK=YYYYMMDDhhmmss,Storage_Capacity=tttttt,Last_Capacity=rrrrrr,len")
set_sysobj = cli.create_parser("CLI=set reset:x,len")
rtc_object = cli.create_parser("CLI=set RTC:YYYYMMDDhhmmss,len")
utc_object = cli.create_parser("CLI=set UTC:YYYYMMDhhmmss,TimeZone,len")
rsoc_object = cli.create_parser("CLI=get SOC:x,len")
mfg_object = cli.create_parser("CLI=set MFG:x pppppppp,len")
get_counter_object = cli.create_parser("CLI=get ResetCounter:ccc,len")
set_counter_object = cli.create_parser("CLI=set ResetCounter:ccc,len")
boot_mode_object = cli.create_parser("CLI=set boot:password,len")
project_mode_object = cli.create_parser("CLI=set mode:mode,len")
information_object = cli.create_parser("CLI=set pi:gender height weight age,len")
file_list_object = cli.create_parser("CLI=get file_list:nnnnnnnn,...,nnnnnnnn,len")
file_size_object = cli.create_parser("CLI=get file_size:ssss,len")
file_contents_object = cli.create_parser("CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n[data 1][data 2]…[data N][Checksum]")
file_remove_object = cli.create_parser("CLI=rm file:nnnnnnnn,len")
test_file_object = cli.create_parser("CLI=file_test:nnn,sss,ccc,len")
binary_object = cli.create_parser("CLI=get dat_char:999,1,25,16,4,250,250,24,2400,6.000000,0.000000,1,1,180,70,25,79")
binary_object = cli.create_parser("CLI=get dat_char:998,077F,26")
binary_object = cli.create_parser("CLI=get dat_char:3,4,21")
stop_send_binary_object = cli.create_parser("CLI=stop dat:len")
stop_send_cmp_object = cli.create_parser("CLI=stop dat_cmp:len")
set_ecg_package_object = cli.create_parser("CLI=set dat_eps:size,len")
get_ecg_package_object = cli.create_parser("CLI=get dat_eps:size,len")
calbri_acc_object = cli.create_parser("CLI=start calib:sel,len")
montion_datarate_object = cli.create_parser("CLI=set odr:rate,len")
get_sensor_range_object = cli.create_parser("CLI=get range:x rang,len")

set_sensor_range_object = cli.create_parser("CLI=set range:x rang,len")
    
# #     print(set_sensor_range_object.cmd)
# #     print(cli.type)
# #     print(cli.parameters)
   
# # except Exception as msg:
# #     print("false")
# #     print(msg)





print("_"*50)
print("get_sysobj type:", type(get_sysobj), "get_sysobj name:", get_sysobj.cmd, "\nmac:", get_sysobj.mac, "\nProject_Name:", get_sysobj.project_name)
print("_"*50)
print("rtc_obj type:",type(rtc_object), "\nrtc_date:", rtc_object.date)
print("_"*50)
print("utc_obj type:",type(utc_object), "\nutc_date:", utc_object.date)
print("_"*50)
print("rsoc_obj type:", type(rsoc_object), "\nrsoc_rsoc:", rsoc_object.rsoc)
print("_"*50)
print("mfg_obj type:", type(mfg_object), "\nmfg_password:", mfg_object.password)
print("_"*50)
print("counter_obj type:", type(get_counter_object), "\nget counter value:", get_counter_object.counter_value)
print("_"*50)
print("counter_obj type:", type(set_counter_object), "\nset counter value:", set_counter_object.set_counter_value)
print("_"*50)
print("boot_mode_obj type:", type(boot_mode_object), "\nbood_mode password:", boot_mode_object.password)
print("_"*50)
print("project_mode_obj type:", type(project_mode_object), "\nproject_mode:", project_mode_object.mode)
print("_"*50)
print("information_obj type:", type(information_object), "\ngender:", information_object.gender, "\nheight:", information_object.height)
print("_"*50)
print("get_filelist_obj type:", type(file_list_object), "\nfile_list:", file_list_object.list_array)
print("_"*50)
print("get_filesize_obj type:", type(file_size_object), "\nfile_size:", file_size_object.file_size)
print("_"*50)
print("get_filecontents_obj type:", type(file_contents_object), "\nfile_name:", file_contents_object.file_name, "\nfile_contents:", file_contents_object.file_content)
print("_"*50)
print("file_remove_obj type:", type(file_remove_object), "\nfile_name:", file_remove_object.file_name)
print("_"*50)
print("file_test_obj type:", type(test_file_object), "\nfile_name:", test_file_object.file_name)
print("_"*50)
print("binary_obj type:", type(binary_object), "\nsupport_dict:", binary_object.support_dic)
print("binary_obj type:", type(binary_object), "\nval:", binary_object.val)
print("_"*50)
print("stop_send_dat_obj type:", type(stop_send_binary_object), "\nlen:", stop_send_binary_object.len)
print("_"*50)
print("stop_send_cmp_obj type:", type(stop_send_cmp_object), "\nlen:", stop_send_cmp_object.len)
print("_"*50)
print("set_ecg_package_obj type:", type(set_ecg_package_object), "\nsize:", set_ecg_package_object.size)
print("_"*50)
print("get_ecg_package_obj type:", type(get_ecg_package_object), "\nsize:", get_ecg_package_object.size)
print("_"*50)
print("calbri_acc_obj type:", type(calbri_acc_object), "\nsel:", calbri_acc_object.sel)
print("_"*50)
print("montion_datarate_obj type:", type(montion_datarate_object), "\nrate:", montion_datarate_object.rate)
print("_"*50)
print("get_sensor_range_obj type:", type(get_sensor_range_object), "\nrange:", get_sensor_range_object.range)
print("_"*50)
print("set_sensor_range_obj type:", type(set_sensor_range_object), "\nrange:", set_sensor_range_object.range)
print("_"*50)

