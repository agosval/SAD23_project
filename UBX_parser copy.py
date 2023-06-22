from serial import Serial
from pyubx2 import UBXReader,ubxhelpers,SET,UBXMessage

file1 = open('myfile.txt', 'w')

try:
    stream = open('COM10___115200_221206_130405.ubx', 'rb')
    ubr = UBXReader(stream, protfilter=2)
    print(type(ubr))
    i=1   # nel file di esempio ci sono 2516 messaggi 
    for (raw_data, parsed_data) in ubr:
        #print(parsed_data.identity)
        file1.write(parsed_data.identity + "\n")
    
except KeyboardInterrupt:
    print("Terminated by user")
    
file1.close()