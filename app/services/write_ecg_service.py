import numpy as np
import wfdb
import os
import json
from sqlalchemy.orm import Session

class WriteEcgService:
    async def create_ecg_records(data):

        signal_data = data["signals_data"]
        Lead_I = signal_data["Lead_I"]
        Lead_II = signal_data["lead_II"]
        Lead_V1 = signal_data["lead_V1"]
        Lead_V2 = signal_data["lead_V2"]
        Lead_V3 = signal_data["lead_V3"]
        Lead_V4 = signal_data["lead_V4"]
        Lead_V5 = signal_data["lead_V5"]
        Lead_V6 = signal_data["lead_V6"]

        lead_data = {
            "lead I": signal_data['Lead_I'],
            "lead II": signal_data['Lead_II'],
            "lead V1": signal_data['Lead_V1'],
            "lead V2": signal_data['Lead_V2'],
            "lead V3": signal_data['Lead_V3'],
            "lead V4": signal_data['Lead_V4'],
            "lead V5": signal_data['Lead_V5'],
            "lead V6": signal_data['Lead_V6']
        }

        print (len(lead_data))
        record_name = data["record_name"]
        sample_frequency = data["sampling_frequency"]
        number_of_samples = data["number_of_samples"]
        d_signal = np.array([Lead_I, Lead_II, Lead_V1, Lead_V2, Lead_V3, Lead_V4, Lead_V5, Lead_V6]).T
        print(d_signal)
        # json_data = json.dumps(d_signal.tolist(), indent=4)

        # # Write the JSON data to a file
        # with open('data1.json', 'w') as json_file:
        #     json_file.write(json_data)

        sig_names = ['I', 'II', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
        fmt = ['32'] * len(sig_names)
        gain = [1] * len(sig_names)
        baseline = [0] * len(sig_names)
        units=['mV'] * len(sig_names)

        if not os.path.exists(os.path.join(os.getcwd(), "dataset", record_name)):
                os.makedirs(os.path.join(os.getcwd(), "dataset", record_name))

        working_dir = os.path.join(os.getcwd(), "dataset", record_name)

        wfdb.wrsamp(record_name, fs = sample_frequency, units=units,
                        sig_name=sig_names, d_signal=d_signal, fmt=fmt, adc_gain=gain, baseline=baseline, write_dir=working_dir)