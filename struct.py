from _struct import *

# Convert to Byte Data
packed_data = pack('iif', 23, 31, 45.84)
print(packed_data)
print(calcsize('iif'))


# Converting to Original
unpacked_data = unpack('iif', packed_data)
print(unpacked_data)
