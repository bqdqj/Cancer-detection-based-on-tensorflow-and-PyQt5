import os
import cv2 as cv
import pandas as pd
from config import record_csv, record_path


class Patient:
    def __init__(self, serial_num=None, date=None, diagnose_result=None):
        self.index = None
        self.serial_num = serial_num
        self.date = date
        self.image = None
        self.image_path = None
        self.diagnose_result = diagnose_result

    def get_properties(self, serial_num=None, date=None, diagnose_result=None):
        self.serial_num = str(serial_num)
        self.date = str(date)
        self.diagnose_result = str(diagnose_result)

    def read_patient_image(self, image_path):
        self.image_path = image_path
        self.image = cv.imread(image_path)

    def save_patient_information(self):
        try:
            os.chdir(record_path)
        except:
            pass
        if os.path.isfile(record_csv):
            df = pd.read_csv(record_csv, encoding='utf-8', dtype=str)
            self.index = len(df) + 1
            df = df.append([{'index': self.index,
                             'serial_number': self.serial_num,
                             'date': self.date,
                             'diagnose_result': self.diagnose_result
                             }])
            df.to_csv(record_csv, index=False)
        else:
            self.index = 1
            df = pd.DataFrame(columns=('index', 'serial_number', 'date', 'diagnose_result'), dtype=str)
            df = df.append([{'index':self.index,
                             'serial_number':self.serial_num,
                             'date':self.date,
                             'diagnose_result':self.diagnose_result,
                             }])
            df.to_csv(record_csv, index=False)

    def update_patient_diagnose(self):
        try:
            os.chdir(record_path)
        except:
            pass
        df = pd.read_csv(record_csv, encoding='utf-8', dtype=str)
        for i, (num, result) in enumerate(zip(df['serial_number'], df['diagnose_result'])):
            if num == self.serial_num:
                df['diagnose_result'][i] = self.diagnose_result
        print(df)
        df.to_csv(record_csv, index=False)
        if self.image is not None:
            cv.imwrite(os.path.join(record_path, self.serial_num + '.png'), self.image)

    def get_patient_information(self, serial_num):
        df = pd.read_csv(os.path.join(record_path, record_csv), encoding='utf-8', dtype=str)
        self.serial_num = serial_num
        try:
            self.date = df.loc[df['serial_number'] == serial_num]['date'].values[0]
            self.diagnose_result = df.loc[df['serial_number'] == serial_num]['diagnose_result'].values[0]
            self.index = df.loc[df['serial_number'] == serial_num]['index'].values[0]
            return True
        except:
            return False

    def show_all_patients_information(self):
        os.startfile(os.path.join(record_path, record_csv))