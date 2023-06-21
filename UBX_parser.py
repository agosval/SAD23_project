from serial import Serial
from pyubx2 import UBXReader,ubxhelpers,SET,UBXMessage


try:
    stream = open('COM10___115200_221206_130405.ubx', 'rb')
    ubr = UBXReader(stream, protfilter=2)
    print(type(ubr))
    for i in range(1,50):
        (raw_data,parsed_data)= ubr.read()
        #print(parsed_data)
        temp= parsed_data.identity
        #print(temp)
        if temp == "NAV-HPPOSLLH" :
            lat, lon, alt = parsed_data.lat, parsed_data.lon, parsed_data.hMSL
            print(f"lat = {lat}, lon = {lon}, alt = {alt/1000} m")
        elif temp == "NAV-STATUS" :
            print(f"STATUS m")
            
            
except KeyboardInterrupt:
    print("Terminated by user")
     




