from .headers import *

def format_size(size) -> str:
    if size < 1024:
        return str(size) + "B"
    elif size < 1024**2:
        return str("{:.2f}".format(size/1024)) + "KB"
    elif size < 1024**3:
        return str("{:.2f}".format(size/(1024**2))) + "MB"
    elif size < 1024**4:
        return str("{:.2f}".format(size/(1024**3))) + "GB"
    else:
        return str("{:.2f}".format(size/(1024**4))) + "TB"

def list_files(filename) -> dict:
    data = dict()
    f = open(filename, 'rb')
    
    #Read header info
    header_start = f.read(5)
    if header_start != FILE_HEADER_START:
        print("Invalid File Format")
        exit(1)
    else:
        print("Dillu File Format Detected")
    
    f.read(3)
    header_version = f.read(5)
    header_version = header_version.decode()
    if header_version not in versions:
        print("Invalid File Version")
        exit(1)
    else:
        print("Version: " + header_version)
    
    f.read(3)
    file_size = int.from_bytes(f.read(8), byteorder='big')
    print("File Size: " + format_size(file_size))

    print()
    no_of_files = int.from_bytes(f.read(8), byteorder='big')
    print("No of Files: " + str(no_of_files))

    offset_start = int.from_bytes(f.read(8), byteorder='big')
    offset_end = int.from_bytes(f.read(8), byteorder='big')
    print("Offset Start: " + str(offset_start))
    print("Offset End: " + str(offset_end))
    data["offsets"] = [offset_start, offset_end]
    print()
    print("Files:")
    for i in range(no_of_files):
        name_size = int.from_bytes(f.read(4), byteorder='big')
        file_name = f.read(name_size - 4 - 8)
        file_size = int.from_bytes(f.read(8), byteorder='big')
        print(file_name.decode() + " : " + format_size(file_size))
        data[file_name.decode()] = [file_size, name_size]

    f.close()
    return data