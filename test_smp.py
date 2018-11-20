import unittest
import datfile_convert_smpa


class TestDatfile(unittest.TestCase):
    def setUP(self):
        self.file_version = b"\x54\x68\x44\x59\x88"
        self.utc_time_zone = b"\x54\x68\x44\x59\x88"
        self.mac_address = b"\x54\x68\x44\x59\x88"
        self.sleep_mode = b"\x54\x68\x44\x59\x88"
        self.posture_log = b"\x54\x68\x44\x59\x88"
        self.file_type = 41
        self.daily_file_name = "TEST"
   
    def tearDown(self):
        pass

    def test_smpa_file_convert(self):
        file_name = "D:\\raw_data\ACC_20181108112354_443DBD.dat"
        file_dir = "D:"
        result = datfile_convert_smpa.smart_life_data_process(file_name, file_dir)
        self.assertEqual(result, True)


    def test_convert_acc(self):
        file_name = "D:\\raw_data\ACC_20181108112354_443DBD.dat"
        file_dir = "D:"
        result = datfile_convert_smpa._convert_acc_raw_data(file_name, file_dir)
        self.assertEqual(result, True)

    def test_convert_ecg(self):
        file_name = "D:\\raw_data\ECG_2018110216_323E.dat"
        file_dir = "D:"
        result = datfile_convert_smpa._convert_ecg_raw_data(file_name, file_dir)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()