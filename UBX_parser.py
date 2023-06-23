from pyubx2 import UBXReader
import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['db_sad']
col_NAV_HPPOSLLH = db['NAV_HPPOSLLH']
col_NAV_HPPOSECEF = db['NAV_HPPOSECEF']
col_NAV_STATUS = db['NAV_STATUS']



print('Available database -> ', client.list_database_names())
print('Available collections -> ', db.list_collection_names())

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
            iTOW,lat, lon, alt = parsed_data.iTOW, parsed_data.lat, parsed_data.lon, parsed_data.hMSL
            document = {"iTOW": iTOW,"lat": lat,"lon": lon, "alt": alt}
            result = col_NAV_HPPOSLLH.update({"iTOW": iTOW},document,upsert=True)
            NAV_HPPOSLLH_f.write(f"iTOW: {iTOW}, lat = {lat}, lon = {lon}, alt = {alt} mm"+ "\n")
        elif id == "NAV-HPPOSECEF":
            iTOW = parsed_data.iTOW
            document = {"iTOW": iTOW}
            result = col_NAV_HPPOSECEF.update({"iTOW": iTOW},document,upsert=True)
            NAV_HPPOSECEF_f.write(parsed_data.identity + "\n")
        elif id == "NAV-STATUS":
            iTOW = parsed_data.iTOW
            document = {"iTOW": iTOW}
            result = col_NAV_STATUS.update({"iTOW": iTOW},document,upsert=True)
            NAV_STATUS_f.write(parsed_data.identity + "\n")
except KeyboardInterrupt:
    print("Terminated by user")
     
all_message_f.close()
NAV_HPPOSLLH_f.close()
NAV_HPPOSECEF_f.close()
NAV_STATUS_f.close()
