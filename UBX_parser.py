from pyubx2 import UBXReader

all_message_f = open('all_message.txt', 'w')
NAV_HPPOSLLH_f = open('NAV_HPPOSLLH.txt', 'w')
NAV_HPPOSECEF_f = open('NAV_HPPOSECEF.txt', 'w')
NAV_STATUS_f = open('NAV_STATUS.txt', 'w')

try:
    stream = open('COM10___115200_221206_130405.ubx', 'rb')
    ubr = UBXReader(stream, protfilter=2,quitonerror = 0)
    print(type(ubr))
    
    for (raw_data, parsed_data) in ubr:   # nel file di esempio ci sono 2516 messaggi 
        id= parsed_data.identity
        all_message_f.write(parsed_data.identity + "\n")
        if id == "NAV-HPPOSLLH" :
            lat, lon, alt = parsed_data.lat, parsed_data.lon, parsed_data.hMSL
            print(f"lat = {lat}, lon = {lon}, alt = {alt} mm")
            NAV_HPPOSLLH_f.write(f"lat = {lat}, lon = {lon}, alt = {alt} mm"+ "\n")
        elif id == "NAV-HPPOSECEF":
            print(f"HPPO")
            NAV_HPPOSECEF_f.write(parsed_data.identity + "\n")
        elif id == "NAV-STATUS":
            print(f"STATUS ")
            NAV_STATUS_f.write(parsed_data.identity + "\n")
except KeyboardInterrupt:
    print("Terminated by user")
     
all_message_f.close()
NAV_HPPOSLLH_f.close()
NAV_HPPOSECEF_f.close()
NAV_STATUS_f.close()
