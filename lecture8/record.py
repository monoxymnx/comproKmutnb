import struct
records = (1, 'John Doe', 20, 3.75)
with open("records.bin","wb") as file:
    data = struct.pack('i20sif', records[0] ,records[1].encode()
            ,records[2],records[3])
    file.write(data)