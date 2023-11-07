import numpy as np
import wfdb
import os
import json
from sqlalchemy.orm import Session
from IPython.display import display

class WriteEcgService:
    async def create_ecg_lead1_record(data):
      try:
        Lead_I = data["lead_one"]
        extension = data['extension']
        sample = data['sample']
        symbol = data['symbol']
        # print(sample)
        # print(symbol)
        # qrst_cycles = data['qrst_cycles']

        lead_data = {
            "lead I": Lead_I,
        }

        # print (len(lead_data))
        record_name = data["record_name"]
        sample_frequency = data["sampling_frequency"]
        number_of_samples = data["number_of_samples"]
        p_signal = np.array([Lead_I]).T
        # print(d_signal)
        # json_data = json.dumps(d_signal.tolist(), indent=4)

        # # Write the JSON data to a file
        # with open('data1.json', 'w') as json_file:
        #     json_file.write(json_data)

        sig_names = ['ECG-Lead-I']
        fmt = ['32'] * len(sig_names)
        gain = [1] * len(sig_names)
        baseline = [0] * len(sig_names)
        units=['mV'] * len(sig_names)

        if not os.path.exists(os.path.join(os.getcwd(), "dataset", record_name)):
                os.makedirs(os.path.join(os.getcwd(), "dataset", record_name))

        working_dir = os.path.join(os.getcwd(), "dataset", record_name)

        wfdb.wrsamp(record_name, fs = sample_frequency, units=units,
                        sig_name=sig_names, p_signal=p_signal, fmt=fmt, adc_gain=gain, baseline=baseline, write_dir=working_dir)

        ann = wfdb.Annotation(record_name, extension, sample, symbol)

        annotations = ann.__dict__

        wfdb.wrann(annotations['record_name'], annotations['extension'], annotations['sample'], annotations['symbol'],
                   subtype=None, chan=None, num=None, aux_note=None, label_store=None, fs=None, custom_labels=None, write_dir=working_dir)

        return True

      except Exception as e:
        raise e

##################################################################################################################################

    async def create_ecg_lead6_record(data):

        Lead_I   = data["lead_one"]
        Lead_II  = data["lead_two"]
        Lead_III = data["lead_three"]
        Lead_aVR = data["lead_avr"]
        Lead_aVF = data["lead_avf"]
        Lead_aVL = data["lead_avl"]
        extension = data['extension']
        sample = data['sample']
        symbol = data['symbol']

        lead_data = {
            "lead I": Lead_I,
            "lead II": Lead_II,
            "lead_III": Lead_III,
            "lead_aVR": Lead_aVR,
            "lead_aVF": Lead_aVF,
            "lead_aVL": Lead_aVL
        }

        print (len(lead_data))
        record_name = data["record_name"]
        sample_frequency = data["sampling_frequency"]
        number_of_samples = data["number_of_samples"]
        p_signal = np.array([Lead_I, Lead_II, Lead_III, Lead_aVR, Lead_aVF, Lead_aVL]).T
        # print(d_signal)
        # json_data = json.dumps(d_signal.tolist(), indent=4)

        # # Write the JSON data to a file
        # with open('data1.json', 'w') as json_file:
        #     json_file.write(json_data)

        sig_names = ['ECG Lead I', 'ECG Lead II', 'ECG Lead III' 'ECG Lead aVR', 'ECG Lead aVF', 'ECG Lead aVL']
        fmt = ['32'] * len(sig_names)
        gain = [1] * len(sig_names)
        baseline = [0] * len(sig_names)
        units=['mV'] * len(sig_names)

        if not os.path.exists(os.path.join(os.getcwd(), "dataset", record_name)):
                os.makedirs(os.path.join(os.getcwd(), "dataset", record_name))

        working_dir = os.path.join(os.getcwd(), "dataset", record_name)

        wfdb.wrsamp(record_name, fs = sample_frequency, units=units,
                        sig_name=sig_names, p_signal=p_signal, fmt=fmt, adc_gain=gain, baseline=baseline, write_dir=working_dir)

        ann = wfdb.Annotation(record_name, extension, sample, symbol)

        annotations = ann.__dict__

        wfdb.wrann(annotations['record_name'], annotations['extension'], annotations['sample'], annotations['symbol'],
                   subtype=None, chan=None, num=None, aux_note=None, label_store=None, fs=None, custom_labels=None, write_dir=working_dir)

        return True

#########################################################################################################################################

    async def create_ecg_lead12_record(data):

        Lead_I   = data["lead_one"]
        Lead_II  = data["lead_two"]
        Lead_III = data["lead_three"]
        Lead_aVR = data["lead_avr"]
        Lead_aVF = data["lead_avf"]
        Lead_aVL = data["lead_avl"]
        Lead_V1 = data["lead_v1"]
        Lead_V2 = data["lead_v2"]
        Lead_V3 = data["lead_v3"]
        Lead_V4 = data["lead_v4"]
        Lead_V5 = data["lead_v5"]
        Lead_V6 = data["lead_v6"]
        extension = data['extension']
        sample = data['sample']
        symbol = data['symbol']


        lead_data = {
            "lead I": Lead_I,
            "lead II": Lead_II,
            "lead_III": Lead_III,
            "lead_aVR": Lead_aVR,
            "lead_aVF": Lead_aVF,
            "lead_aVL": Lead_aVL,
            "lead V1": Lead_V1,
            "lead V2": Lead_V2,
            "lead V3": Lead_V3,
            "lead V4": Lead_V4,
            "lead V5": Lead_V5,
            "lead V6": Lead_V6
        }

        print (len(lead_data))
        record_name = data["record_name"]
        sample_frequency = data["sampling_frequency"]
        number_of_samples = data["number_of_samples"]
        p_signal = np.array([Lead_I, Lead_II, Lead_III, Lead_aVR, Lead_aVF, Lead_aVL, Lead_V1, Lead_V2, Lead_V3, Lead_V4, Lead_V5, Lead_V6]).T
        # print(d_signal)
        # json_data = json.dumps(d_signal.tolist(), indent=4)

        # # Write the JSON data to a file
        # with open('data1.json', 'w') as json_file:
        #     json_file.write(json_data)

        sig_names = ['ECG Lead I',
                     'ECG Lead II',
                     'ECG Lead III'
                     'ECG Lead aVR',
                     'ECG Lead aVF',
                     'ECG Lead aVL',
                     'ECG Lead V1',
                     'ECG Lead V2',
                     'ECG Lead V3',
                     'ECG Lead V4',
                     'ECG Lead V5',
                     'ECG Lead V6']
        fmt = ['32'] * len(sig_names)
        gain = [1] * len(sig_names)
        baseline = [0] * len(sig_names)
        units=['mV'] * len(sig_names)

        if not os.path.exists(os.path.join(os.getcwd(), "dataset", record_name)):
                os.makedirs(os.path.join(os.getcwd(), "dataset", record_name))

        working_dir = os.path.join(os.getcwd(), "dataset", record_name)

        wfdb.wrsamp(record_name, fs = sample_frequency, units=units,
                        sig_name=sig_names, p_signal=p_signal, fmt=fmt, adc_gain=gain, baseline=baseline, write_dir=working_dir)

        ann = wfdb.Annotation(record_name, extension, sample, symbol)

        annotations = ann.__dict__

        wfdb.wrann(annotations['record_name'], annotations['extension'], annotations['sample'], annotations['symbol'],
                   subtype=None, chan=None, num=None, aux_note=None, label_store=None, fs=None, custom_labels=None, write_dir=working_dir)

        return True