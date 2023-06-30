from pyubx2 import UBXReader
import json
import time
from os import path


all_message_f = open('all_message.txt', 'w')
NAV_HPPOSLLH_f = open('NAV_HPPOSLLH.txt', 'w')
NAV_HPPOSECEF_f = open('NAV_HPPOSECEF.txt', 'w')
NAV_STATUS_f = open('NAV_STATUS.txt', 'w')

listObj = []
#NAV_HPPOSLLH_json = open('NAV_HPPOSLLH.json', 'w')
#listObj = json.load(NAV_HPPOSLLH_json)
with open('NAV_HPPOSLLH_json.json','w') as fp: fp.write('[]')
with open('NAV_HPPOSLLH_json.json') as fp: listObj = json.load(fp)
    

try:
    #stream = open('COM10___115200_221206_130405.ubx', 'rb')
    stream = open('COM6___115200_230517_115332.ubx','rb')
    ubr = UBXReader(stream, protfilter=2,quitonerror = 0)
    print(type(ubr))
    listObj = []
    for (raw_data, parsed_data) in ubr:   
        #id= parsed_data.identity
        #all_message_f.write(parsed_data.identity + "\n")
        if not hasattr(parsed_data, "identity"):
            print("obj has attribute 'identity'")
        elif parsed_data.identity == "NAV-HPPOSLLH" :
            version,invalidLlh,iTOW,lon,lat,height,hMSL,hAcc,vAcc =   parsed_data.version,parsed_data.invalidLlh,parsed_data.iTOW,parsed_data.lon,parsed_data.lat,parsed_data.height,parsed_data.hMSL,parsed_data.hAcc,parsed_data.vAcc
            #data = {'NAV_HPPOSLLH':[{'version': version, 'invalidLlh': invalidLlh, 'iTOW': iTOW, 'lon': lon, 'lat': lat, 'height': height, 'hMSL': hMSL, 'hAcc': hAcc, 'vAcc': vAcc }]}
            data = {'version': version, 'invalidLlh': invalidLlh, 'iTOW': iTOW, 'lon': lon, 'lat': lat, 'height': height, 'hMSL': hMSL, 'hAcc': hAcc, 'vAcc': vAcc }
            listObj.insert(0,data)
            with open('NAV_HPPOSLLH_json.json', 'w') as json_file:
                json.dump(listObj, json_file,indent=4, separators=(',',': '))
            NAV_HPPOSLLH_f.write(f"version = {version},invalidLlh = {invalidLlh},iTOW = {iTOW},lon={lon},lat={lat},height={height},hMSL={hMSL},hAcc={hAcc},vAcc={vAcc}"+ "\n")
            #json_string = json.dumps(listObj, indent=1)
            #NAV_HPPOSLLH_json.write(json_string)
        elif parsed_data.identity == "NAV-HPPOSECEF":
            iTOW = parsed_data.iTOW
            #document = {"iTOW": iTOW}
            #result = col_NAV_HPPOSECEF.update({"iTOW": iTOW},document,upsert=True)
            NAV_HPPOSECEF_f.write(parsed_data.identity + "\n")
        elif parsed_data.identity == "NAV-STATUS":
            iTOW = parsed_data.iTOW
            #document = {"iTOW": iTOW}
            #result = col_NAV_STATUS.update({"iTOW": iTOW},document,upsert=True)
            NAV_STATUS_f.write(parsed_data.identity + "\n")
        else:
            all_message_f.write(parsed_data.identity + "\n")
            time.sleep(0.05)
except KeyboardInterrupt:
    print("Terminated by user")
     
all_message_f.close()
NAV_HPPOSLLH_f.close()
NAV_HPPOSECEF_f.close()
NAV_STATUS_f.close()

#NAV_HPPOSLLH_json.close()

