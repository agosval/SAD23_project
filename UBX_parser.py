from serial import Serial
from pyubx2 import UBXReader,ubxhelpers,SET,UBXMessage


try:
    stream = open('COM10___115200_221206_130405.ubx', 'rb')
    ubr = UBXReader(stream, protfilter=2)
    print(type(ubr))
    
    for i in ubr:
        (raw_data,parsed_data)= ubr.read()
        #print(parsed_data)
        id= parsed_data.identity
        #print(temp)
        if id == "NAV-HPPOSLLH" :
            lat, lon, alt = parsed_data.lat, parsed_data.lon, parsed_data.hMSL
            print(f"lat = {lat}, lon = {lon}, alt = {alt/1000} m")
        elif id == "HPPOSECEF":
            print(f"HPPO")
        elif id == "NAV-STATUS" :
            print(f"STATUS ")
            
            
except KeyboardInterrupt:
    print("Terminated by user")
     




