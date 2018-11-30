import parser_class

class CliResponseParser():
    def __init__(self):
        
        self.cmd = None
        self.parameters = None        
        self.map_dic = {
        "CLI=get status": parser_class.SysGetStatus(),
        "CLI=set reset": parser_class.SysSetSystem(),
        "CLI=set RTC": parser_class.SysSetRtc(),
        "CLI=get RTC": parser_class.SysGetRtc(),
        "CLI=set UTC": parser_class.SysSetUtc(),
        "CLI=get UTC": parser_class.SysGetUtc(),
        "CLI=get SOC": parser_class.SysGetRsoc(),
        "CLI= set MFG": parser_class.SysSetManufactureCode(),
        "CLI= get ResetCounter": parser_class.SysGetResetCounter(),
        "CLI= set ResetCounter": parser_class.SysSetResetCounter(),
        "CLI=set boot": parser_class.SystSetSystemModetoBootMode(),
        "CLI=set mode": parser_class.SysSetProjectMode(),
        "CLI= set pi": parser_class.SysSetPersonalInformation(),
        "CLI=get file_list": parser_class.SysGetFileList(),
        "CLI=get file_size": parser_class.SysGetFileSize(),
        "CLI=get file_contents": parser_class.SysGetFileContents(),
         }
        
    def _mapping_parser(self, cmd, parameters):
        parser_object = self.map_dic.get(cmd)
        parser_object.attribute_parser(parameters, cmd)
        return parser_object       

    def _cli_cmd(self, input_repsonse):
        try:
            cmd_list = input_repsonse.split(":")
            self.cmd = cmd_list[0]
            self.parameters = cmd_list[1]
        except:
            return False

    def create_parser(self, input_repsonse):
        self._cli_cmd(input_repsonse)
        return self._mapping_parser(self.cmd, self.parameters)


   

#Test code
cli = CliResponseParser()
get_sysobj = cli.create_parser("CLI=get status:MAC=xx.xx.xx.xx.xx.xx,Project_Name=nnnnnn,CLI_Version=Vc,Boot_Version=Vb.b.b,HW_Version=Vh.h.h,FW_Version=Vf.f.f,CLOCK=YYYYMMDDhhmmss,Storage_Capacity=tttttt,Last_Capacity=rrrrrr,len")
set_sysobj = cli.create_parser("CLI=set reset:x,len")
rtc_object = cli.create_parser("CLI=set RTC:YYYYMMDDhhmmss,len")
utc_object = cli.create_parser("CLI=set UTC:YYYYMMDhhmmss,TimeZone,len")
rsoc_object = cli.create_parser("CLI=get SOC:x,len")
mfg_object = cli.create_parser("CLI= set MFG:x pppppppp,len")
get_counter_object = cli.create_parser("CLI= get ResetCounter:ccc,len")
set_counter_object = cli.create_parser("CLI= set ResetCounter:ccc,len")
boot_mode_object = cli.create_parser("CLI=set boot:password,len")
project_mode_object = cli.create_parser("CLI=set mode:mode,len")
information_object = cli.create_parser("CLI= set pi:gender height weight age,len")
file_list_object = cli.create_parser("CLI=get file_list:nnnnnnnn,...,nnnnnnnn,len")
file_size_object = cli.create_parser("CLI=get file_size:ssss,len")
file_contents_object = cli.create_parser("CLI=get file_contents:nnnnnnnn,ssss,eeee,len\r\n[data 1][data 2]…[data N][Checksum]")

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










