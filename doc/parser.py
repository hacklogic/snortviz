import os
import binascii


filename = '1.zip'
with open(filename, 'rb') as f:
    content = f.read()
data = binascii.hexlify(content)

print data

data2 = binascii.unhexlify(data)
wp = open("2.zip", 'wb')
wp.write(data2)
wp.close()
