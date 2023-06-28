from pyubx2 import UBXReader
import json
import logging


all_message_f = open('all_message.txt', 'w')
NAV_HPPOSLLH_f = open('NAV_HPPOSLLH.txt', 'w')
NAV_HPPOSECEF_f = open('NAV_HPPOSECEF.txt', 'w')
NAV_STATUS_f = open('NAV_STATUS.txt', 'w')

NAV_HPPOSLLH_json = open('NAV_HPPOSLLH.json', 'w')


try:
    stream = open('COM10___115200_221206_130405.ubx', 'rb')
    ubr = UBXReader(stream, protfilter=2,quitonerror = 0)
    print(type(ubr))
    
    for (raw_data, parsed_data) in ubr:   # nel file di esempio ci sono 2516 messaggi 
        id= parsed_data.identity
        all_message_f.write(parsed_data.identity + "\n")

        if id == "NAV-HPPOSLLH" :
            version,invalidLlh,iTOW,lon,lat,height,hMSL,hAcc,vAcc =   parsed_data.version,parsed_data.invalidLlh,parsed_data.iTOW,parsed_data.lon,parsed_data.lat,parsed_data.height,parsed_data.hMSL,parsed_data.hAcc,parsed_data.vAcc
            data = {'NAV_HPPOSLLH':[{'version': version, 'invalidLlh': invalidLlh, 'iTOW': iTOW, 'lon': lon, 'lat': lat, 'height': height, 'hMSL': hMSL, 'hAcc': hAcc, 'vAcc': vAcc }]}
            NAV_HPPOSLLH_f.write(f"version = {version},invalidLlh = {invalidLlh},iTOW = {iTOW},lon={lon},lat={lat},height={height},hMSL={hMSL},hAcc={hAcc},vAcc={vAcc}"+ "\n")
            json_string = json.dumps(data, indent=1)
            NAV_HPPOSLLH_json.write(json_string)
            logging.config.dictConfig(json_string)
        elif id == "NAV-HPPOSECEF":
            iTOW = parsed_data.iTOW
            #document = {"iTOW": iTOW}
            #result = col_NAV_HPPOSECEF.update({"iTOW": iTOW},document,upsert=True)
            NAV_HPPOSECEF_f.write(parsed_data.identity + "\n")
        elif id == "NAV-STATUS":
            iTOW = parsed_data.iTOW
            #document = {"iTOW": iTOW}
            #result = col_NAV_STATUS.update({"iTOW": iTOW},document,upsert=True)
            NAV_STATUS_f.write(parsed_data.identity + "\n")
except KeyboardInterrupt:
    print("Terminated by user")
     

NAV_HPPOSLLH_json.close()
  
all_message_f.close()
NAV_HPPOSLLH_f.close()
NAV_HPPOSECEF_f.close()
NAV_STATUS_f.close()


