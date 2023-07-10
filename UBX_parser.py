from pyubx2 import UBXReader
import json
import time
from os import path



if __name__ == '__main__':
    all_message_f = open('all_message.txt', 'w')
    NAV_HPPOSLLH_f = open('NAV_HPPOSLLH.txt', 'w')
    NAV_HPPOSECEF_f = open('NAV_HPPOSECEF.txt', 'w')
    NAV_STATUS_f = open('NAV_STATUS.txt', 'w')

    listHPPOSLLH = []
    listHPPOSECEF = []
    listSTATUS = []

    #NAV_HPPOSLLH_json = open('NAV_HPPOSLLH.json', 'w')
    #listHPPOSLLH = json.load(NAV_HPPOSLLH_json)
    data = '[{},{},{},{},{},{},{},{},{},{}]'
    with open('NAV_HPPOSLLH_json.json','w') as fp: fp.write(data)
    with open('NAV_HPPOSLLH_json.json') as fp: listHPPOSLLH = json.load(fp)

    with open('NAV_HPPOSECEF_json.json','w') as fp: fp.write(data)
    with open('NAV_HPPOSECEF_json.json') as fp: listHPPOSECEF = json.load(fp)

    with open('NAV_STATUS_json.json','w') as fp: fp.write(data)
    with open('NAV_STATUS_json.json') as fp: listSTATUS = json.load(fp)

    try:
        #stream = open('COM10___115200_221206_130405.ubx', 'rb')
        stream = open('COM6___115200_230517_115332.ubx','rb')
        ubr = UBXReader(stream, protfilter=2,quitonerror = 0)
        print(type(ubr))
        for (raw_data, parsed_data) in ubr:   
            if not hasattr(parsed_data, "identity"):
                print("obj has attribute 'identity'")
            elif parsed_data.identity == "NAV-HPPOSLLH" :
                version,invalidLlh,iTOW,lon,lat,height,hMSL,hAcc,vAcc =   parsed_data.version,parsed_data.invalidLlh,parsed_data.iTOW,parsed_data.lon,parsed_data.lat,parsed_data.height,parsed_data.hMSL,parsed_data.hAcc,parsed_data.vAcc
                data = {'version': version, 'invalidLlh': invalidLlh, 'iTOW': iTOW, 'lon': lon, 'lat': lat, 'height': height, 'hMSL': hMSL, 'hAcc': hAcc, 'vAcc': vAcc }
                listHPPOSLLH.insert(0,data)
                del listHPPOSLLH[10]
                with open('NAV_HPPOSLLH_json.json', 'w') as json_file:
                    json.dump(listHPPOSLLH, json_file,indent=4, separators=(',',': '))
                NAV_HPPOSLLH_f.write(f"version = {version},invalidLlh = {invalidLlh},iTOW = {iTOW},lon={lon},lat={lat},height={height},hMSL={hMSL},hAcc={hAcc},vAcc={vAcc}"+ "\n")
                time.sleep(0.5)
            elif parsed_data.identity == "NAV-HPPOSECEF":  #non testato per mancanza di dati
                version,iTOW=parsed_data.version,parsed_data.iTOW
                ecefX,ecefY,ecefZ = parsed_data.ecefX,parsed_data.ecefY,parsed_data.ecefZ 
                ecefXHp,ecefYHp,ecefZHp = parsed_data.ecefXHp,parsed_data.ecefYHp,parsed_data.ecefZHp
                invalidEcef,pAcc = parsed_data.invalidEcef,parsed_data.pAcc
                data = {'version': version,'iTOW': iTOW,'ecefX': ecefX, 'ecefY': ecefY, 'ecefZ': ecefZ,'ecefXHp': ecefXHp,'ecefYHp': ecefYHp,'ecefZHp': ecefZHp,'invalidEcef': invalidEcef, 'pAcc': pAcc }
                listHPPOSECEF.insert(0,data)
                del listHPPOSECEF[10]
                with open('NAV_HPPOSECEF_json.json', 'w') as json_file:
                    json.dump(listHPPOSECEF, json_file,indent=4, separators=(',',': '))
                time.sleep(0.5)            
            elif parsed_data.identity  == "NAV-STATUS":
                iTOW,gpsFix = parsed_data.iTOW,parsed_data.gpsFix
                flags = str(parsed_data.gpsFixOk) + str(parsed_data.diffSoln) + str(parsed_data.wknSet) + str(parsed_data.towSet)
                fixStat = str(parsed_data.diffCorr) + str(parsed_data.carrSolnValid) + str(parsed_data.mapMatching) 
                flags2 = str(parsed_data.psmState) + str(parsed_data.spoofDetState) + str(parsed_data.carrSoln)
                ttff,msss= parsed_data.ttff,parsed_data.msss
                #data = {'version': version, 'invalidLlh': invalidLlh, 'iTOW': iTOW, 'lon': lon, 'lat': lat, 'height': height, 'hMSL': hMSL, 'hAcc': hAcc, 'vAcc': vAcc }
                data = {'iTOW': iTOW,'gpsFix': gpsFix,'flags': flags, 'fixStat': fixStat, 'flags2': flags2,'ttff': ttff,'msss': msss }
                listSTATUS.insert(0,data)
                del listSTATUS[10]
                with open('NAV_STATUS_json.json', 'w') as json_file:
                    json.dump(listSTATUS, json_file,indent=4, separators=(',',': '))
                NAV_STATUS_f.write(f"iTOW = {iTOW},gpsFix = {gpsFix},flags = {flags},fixStat={fixStat},flags2={flags2},ttff={ttff},msss={msss}"+ "\n")
                time.sleep(0.5)
            else:
                all_message_f.write(parsed_data.identity + "\n")
                #time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminated by user")
     
all_message_f.close()
NAV_HPPOSLLH_f.close()
NAV_HPPOSECEF_f.close()
NAV_STATUS_f.close()


