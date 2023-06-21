from pyubx2 import UBXReader

stream = open('COM10___115200_221206_130405.ubx', 'rb')
ubr = UBXReader(stream, protfilter=2)

msg = ubr.parse(b'\xb5b\x05\x01\x02\x00\x06\x01\x0f\x38')
print(msg)

msg = UBXReader.parse(b'\xb5b\x01\x12$\x000D\n\x18\xfd\xff\xff\xff\xf1\xff\xff\xff\xfc\xff\xff\xff\x10\x00\x00\x00\x0f\x00\x00\x00\x83\xf5\x01\x00A\x00\x00\x00\xf0\xdfz\x00\xd0\xa6')
print(msg)

msg = UBXReader.parse(b'\xb5b\x01\x12$\x000D\n\x18')
print(msg)