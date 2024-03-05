import zlib, base64


def compress(input_file, output_file):
    
    data = open(input_file, 'r').read()

    #compress using zlib
    #zlib only accepts bytes data + utf-8 hence convert the string data in the sample_text to bytes

    data_bytes = bytes(data, 'utf-8')

    data_bytes_compressed = zlib.compress(data_bytes, 9) #compressing with zlib and setting the level of compression (0-9)

    # to use the data, it has to be encoded using base64.b64encode()
    data_bytes_compressed_encoded = base64.b64encode(data_bytes_compressed)

    #to write the compressed data we need to convert from bytes to strings using decode('utf-8)
    open(output_file, 'w').write(data_bytes_compressed_encoded.decode('utf-8'))

#compress('sample.txt', 'new.txt')


# DECOMPRESSING THE DATA BACK TO READABLE DATA
def decompress(input_file, output_file):
    file_content = open(input_file, 'r').read()
    decompressed_file = zlib.decompress(base64.b64decode(file_content))
    file = open(output_file, 'w')
    file.write(decompressed_file.decode('utf-8'))
    file.close()
    
