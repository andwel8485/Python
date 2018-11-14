import struct
import datetime
import csv

_ECG_RAW_DATA_CHARACTER_LENTH = 32
_ACC_RAW_DATA_CHARACTER_LENTH = 22

_UTC_TYPE = 0
_FILE_FORMAT_VERSION_TYPE = 4
_MAC_ADDRESS_TYPE = 6
_ECG_RAW_DATA_CHARACTER = 32
_TPR_TYPE = 41
_POSTURE_LOG_TYPE = 54
_SLEEP_MODE_TYPE = 80

def _change_time_foramt(t):
    readable = datetime.datetime.fromtimestamp(t)
    _change_time_foramtd = readable.strftime("%Y%m%d%H%M%S")
    return _change_time_foramtd

def _ecg_convert_to_smpa(ecg, ecg_file_name, file_type, utc_start_time,
                         sample_rate, adc_resolution, adc_signed):
    bit = 8
    BYTES = int(adc_resolution / bit)
    time_offset_lenth = 2 
    while True:
        raw_data_list = []
        rate = 1
        time_offset = ecg.read(time_offset_lenth)
        if time_offset == b"":
            break
        time_offset = int.from_bytes(time_offset, byteorder='little', signed=True)
            
        while rate <= sample_rate :
            raw_data = ecg.read(BYTES)
            if raw_data == b"":
                break
            raw_data = int.from_bytes(raw_data, byteorder='little', signed=True)
            raw_data_smpa = [file_type, time_offset, raw_data, " ", " "]
            raw_data_list.append(raw_data_smpa)
            rate += 1
             
        with open(ecg_file_name, 'at', newline='') as ecg_smpa:
            csvout = csv.writer(ecg_smpa)
            csvout.writerows(raw_data_list)

def _tpr_convert_to_smpa(daily_file_name, file_type, tpr_content):
    
    subtype = format(tpr_content[0], "08b")
    mode = int(subtype[:2])
    interval = int(subtype[2:])    
    temp_index = 1
    pulse_index = 2
    respiration_index = 3
    tpr_raw_data_list = []
    
    read = True
    while read:
        try:
            temp, pulse, respiration = (tpr_content[temp_index], tpr_content[pulse_index],
                                        tpr_content[respiration_index])
            tpr_raw_data = [file_type, float(temp / 10), pulse, respiration]
            tpr_raw_data_list.append(tpr_raw_data)
            
            temp_index += 3
            pulse_index += 3
            respiration_index += 3
        except:
            read = False
            break

    with open(daily_file_name, "at", newline="") as tpr_smpa:
        csvout = csv.writer(tpr_smpa)
        csvout.writerows(tpr_raw_data_list)

def _file_format(daily_file_name, file_type, file_version):
    file_format_version = int.from_bytes(file_version, byteorder="little")
    file_format_version_list = [[file_type, file_format_version]]
    
    with open(daily_file_name, "at", newline="") as fmv_smpa:
        csvout = csv.writer(fmv_smpa)
        csvout.writerows(file_format_version_list)

def _utc_time_zone(daily_file_name, file_type, utc_time_zone):
    utc_time = int.from_bytes(utc_time_zone[:4], byteorder="little")
    utc_time_converted = _change_time_foramt(utc_time)
    utc_zone = int.from_bytes(utc_time_zone[4:], byteorder="little")
    utc_time_zone_list = [[file_type, utc_time_converted, utc_zone]]
    
    with open(daily_file_name, "at", newline="") as utc_smpa:
        csvout = csv.writer(utc_smpa)
        csvout.writerows(utc_time_zone_list)

def _mac_address(daily_file_name, file_type, mac_address):
    mc_ad = int.from_bytes(mac_address, byteorder="little")
    mac_address_list = [[file_type, mc_ad]]

    with open(daily_file_name, "at", newline="") as mac_smpa:
        csvout = csv.writer(mac_smpa)
        csvout.writerows(mac_address_list)

def _acc_convert_to_smpa(acc, acc_file_name, file_type, sample_rate, utc_start_time):
    while True:
        time_offset = acc.read(2)
        if time_offset == b"":
            break
        time_offset = int.from_bytes(time_offset, byteorder="little", signed=True)
        acc_raw_data_list = []
        rate = 1 
        multi_sensor_id = 0
        
        while rate <= sample_rate:
            try:
                acce_x, acce_y, acce_z = struct.unpack("<3H", acc.read(6))
                acc_raw_data = [file_type, multi_sensor_id, time_offset, acce_x, acce_y, acce_z]
                acc_raw_data_list.append(acc_raw_data)
                rate += 1
            except:
                break

        with open(acc_file_name, "at", newline="") as acc_smpa:
            csvout = csv.writer(acc_smpa)
            csvout.writerows(acc_raw_data_list)

def smart_life_data_process(file_name, file_dir):
    
    if "ECG" in file_name:
        with open(file_name, "rb") as ecg:
            file_header = ecg.read(_ECG_RAW_DATA_CHARACTER_LENTH)
            file_format_version, utc_start_time, utc_time_zone,  record_interval, \
                file_type, sample_rate, adc_resolution, adc_vref, amp_gain, amp_offset, adc_signed \
                = struct.unpack('<HIB6xIBHBH2IB', file_header)
            mac_address = int.from_bytes(file_header[7:13], byteorder="little")
            file_head_contents = [
                [
                _ECG_RAW_DATA_CHARACTER, sample_rate, adc_resolution,
                adc_vref, amp_gain, amp_offset, adc_signed
                ]
                    ]
            time_list = [[_UTC_TYPE, _change_time_foramt(utc_start_time)]]

            ecg_file_name = file_dir + "\\ECG_" + _change_time_foramt(utc_start_time) + ".smpa"
            with open(ecg_file_name, 'wt', newline ='') as ecg_smpa:
                csvout = csv.writer(ecg_smpa)
                csvout.writerows(file_head_contents)
                csvout.writerows(time_list)

            _ecg_convert_to_smpa(
                ecg, ecg_file_name, file_type, utc_start_time, 
                sample_rate, adc_resolution, adc_signed)

    elif "DAILY" in file_name:
        with open(file_name, "rb") as f:
            daily_file_name = file_dir + file_name.split("\\")[-1][:-5] + ".smpa"
            
            with open(daily_file_name, "wt") as daily_smpa:
                pass

            while True:
                file_type = f.read(1)
                file_lenth = f.read(1)
                if (file_type == b'') and (file_lenth == b''):
                    break
                file_type = int.from_bytes(file_type, byteorder="little")
                file_lenth = int.from_bytes(file_lenth, byteorder="little")

                if file_type == _TPR_TYPE:
                    try:
                        tpr_content = f.read(file_lenth)
                        _tpr_convert_to_smpa(daily_file_name, file_type, tpr_content)
                    except:
                        tpr_content = f.read()
                        _tpr_convert_to_smpa(daily_file_name, file_type, tpr_content)
                        
                elif file_type == _FILE_FORMAT_VERSION_TYPE:
                    file_version = f.read(file_lenth)
                    _file_format(daily_file_name, file_type, file_version)
                            
                elif file_type == _UTC_TYPE:
                    utc_time_zone = f.read(file_lenth)
                    _utc_time_zone(daily_file_name, file_type, utc_time_zone)

                elif file_type == _MAC_ADDRESS_TYPE:
                    mac_address = f.read(file_lenth)
                    _mac_address(daily_file_name, file_type, mac_address)

                elif file_type == _SLEEP_MODE_TYPE:
                    sleep_mode = f.read(file_lenth)

                elif file_type == _POSTURE_LOG_TYPE:
                    ecg_raw_character = f.read(file_lenth)

    elif "ACC" in file_name:
        with open(file_name, "rb") as acc:
            file_header = acc.read(_ACC_RAW_DATA_CHARACTER_LENTH)
            file_format_version, utc_start_time, utc_time_zone, \
                record_interval, file_type, sample_rate, resolution, ranges \
                = struct.unpack('<HIB6xIBH2B', file_header)
            mac_address = int.from_bytes(file_header[7:13], byteorder="little")
            file_head_contents = [
                [
                file_format_version, utc_start_time, utc_time_zone,
                record_interval, file_type, sample_rate, resolution, ranges
                ]
                    ]
            acc_file_name = file_dir + "\\ACC_" + _change_time_foramt(utc_start_time) + ".smpa"
            with open(acc_file_name, "wt", newline="") as acc_smpa:
                csvout = csv.writer(acc_smpa)
                csvout.writerows(file_head_contents)

            _acc_convert_to_smpa(acc, acc_file_name, file_type, sample_rate, utc_start_time)

    



