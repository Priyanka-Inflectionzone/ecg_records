import array
import numpy as np
from app.services.read_ecg_service import ReadEcgService
from app.services.write_ecg_service import WriteEcgService
from fastapi import Request

async def read_ecg_(dataset_dir, record_name, extension, db_session):
    try:
       headers = await ReadEcgService.read_header(db_session, dataset_dir, record_name)
       data = await ReadEcgService.read_signals( db_session, dataset_dir, record_name)
       annotations = await ReadEcgService.read_annotation(db_session, dataset_dir, record_name, extension)
       message = "Records created successfully"
       return headers, data, annotations
    except Exception as e:
        raise e
    finally:
        db_session.close()


async def write_ecg_lead1_(record: Request):
    try:
       record_data = await record.json()
       record_name = record_data.get('RecordName')
       sampling_frequency = record_data.get('SamplingFrequency')
       number_of_samples = record_data.get('NumberOfSamples')
       extension = record_data.get('Extension')
       qrst_cycles = record_data.get('QRSTCycles')
       lead_one = record_data.get('LeadOne')

       symbols = []
       samples = []

       for item in qrst_cycles:
            for key, value in item.items():
                symbols.append(key)
                samples.append(value)
       sample = np.array(samples)
       symbol = np.array(symbols)

       data = {
           "record_name": record_name,
           "sampling_frequency": sampling_frequency,
           "number_of_samples": number_of_samples,
           "extension": extension,
           "sample": sample,
           "symbol": symbol,
           "lead_one": lead_one
           }

       records = await WriteEcgService.create_ecg_lead1_record(data)
       message = "Records created successfully"
       return True
    except Exception as e:
        raise e

async def write_ecg_lead6_(record: Request):
    try:
       record_data = await record.json()
       record_name = record_data.get('RecordName')
       sampling_frequency = record_data.get('SamplingFrequency')
       number_of_samples = record_data.get('NumberOfSamples')
       extension = record_data.get('Extension')
       qrst_cycles = record_data.get('QRSTCycles')
       lead_one = record_data.get('LeadOne')
       lead_two = record_data.get('LeadTwo')
       lead_three = record_data.get('LeadThree')
       lead_avr = record_data.get('Avr')
       lead_avf = record_data.get('Avf')
       lead_avl = record_data.get('Avl')
       symbols = []
       samples = []

       for item in qrst_cycles:
            for key, value in item.items():
                symbols.append(key)
                samples.append(value)
       sample = np.array(samples)
       symbol = np.array(symbols)
       data = {
           "record_name": record_name,
           "sampling_frequency": sampling_frequency,
           "number_of_samples": number_of_samples,
           "extension": extension,
           "sample": sample,
           "symbol": symbol,
           "lead_one": lead_one,
           "lead_two": lead_two,
           "lead_three": lead_three,
           "lead_avr": lead_avr,
           "lead_avf": lead_avf,
           "lead_avl": lead_avl
           }

       records = await WriteEcgService.create_ecg_lead6_record(data)

    except Exception as e:
        raise e

async def write_ecg_lead12_(record: Request):
    try:
       record_data = await record.json()
       record_name = record_data.get('RecordName')
       sampling_frequency = record_data.get('SamplingFrequency')
       number_of_samples = record_data.get('NumberOfSamples')
       extension = record_data.get('Extension')
       qrst_cycles = record_data.get('QRSTCycles')
       lead_one = record_data.get('LeadOne')
       lead_two = record_data.get('LeadTwo')
       lead_three = record_data.get('LeadThree')
       lead_avr = record_data.get('Avr')
       lead_avf = record_data.get('Avf')
       lead_avl = record_data.get('Avl')
       lead_v1 = record_data.get('V1')
       lead_v2 = record_data.get('V2')
       lead_v3 = record_data.get('V3')
       lead_v4 = record_data.get('V4')
       lead_v5 = record_data.get('V5')
       lead_v6 = record_data.get('V6')
       symbols = []
       samples = []

       for item in qrst_cycles:
            for key, value in item.items():
                symbols.append(key)
                samples.append(value)
       sample = np.array(samples)
       symbol = np.array(symbols)
       data = {
           "record_name": record_name,
           "sampling_frequency": sampling_frequency,
           "number_of_samples": number_of_samples,
           "extension": extension,
           "sample": sample,
           "symbol": symbol,
           "lead_one": lead_one,
           "lead_two": lead_two,
           "lead_three": lead_three,
           "lead_avr": lead_avr,
           "lead_avf": lead_avf,
           "lead_avl": lead_avl,
           "lead_v1": lead_v1,
           "lead_v2": lead_v2,
           "lead_v3": lead_v3,
           "lead_v4": lead_v4,
           "lead_v5": lead_v5,
           "lead_v6": lead_v6
           }

       records = await WriteEcgService.create_ecg_lead12_record(data)

    except Exception as e:
        raise e