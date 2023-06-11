from misc import headers
import os

def get_indexing_data(filename):
    index_metadata_size = 0
    total_size = 0
    file_size = 0
    index_data = dict()

    if os.path.isfile(filename):
        #directory name : file size
        name = os.path.basename(filename)
        index_metadata_size += len(name) + 8 + 4
        file_size += os.path.getsize(filename)
        index_data[name] = [file_size, index_metadata_size]
        return index_data, file_size, index_metadata_size
    
    else:
        for path, _, files in os.walk(filename):
            for file in files:
                file_path = os.path.join(path, file)
                index_metadata_size += len(file_path) + 8 + 4
                file_size = os.path.getsize(file_path)
                total_size += file_size
                index_data[file_path] = [file_size, len(file_path) + 8 + 4]
        return index_data, total_size, index_metadata_size
            


def export_file(filename, output_filename):
    print("Exporting file " + output_filename + "...\n")
    index_data, total_size, index_metadata_size = get_indexing_data(filename)

    with open(output_filename, 'wb') as f:
        #Write header info
        f.write(headers.FILE_HEADER_START)
        f.write(headers.FILE_HEADER_PADDING)
        f.write(headers.FILE_HEADER_VERSION)
        f.write(headers.FILE_HEADER_VERSION_PADDING)

        #write size, data offset and indexing info
        headers.THIS_FILE_SIZE += index_metadata_size + total_size
        f.write(headers.THIS_FILE_SIZE.to_bytes(8, byteorder='big'))

        NO_OF_FILES = len(index_data)
        f.write(NO_OF_FILES.to_bytes(8, byteorder='big'))

        headers.OFFSET_START += index_metadata_size
        f.write(headers.OFFSET_START.to_bytes(8, byteorder='big'))

        headers.OFFSET_END += headers.OFFSET_START + total_size 
        f.write(headers.OFFSET_END.to_bytes(8, byteorder='big'))

        #write file index info
        for file_name, file_size in index_data.items():
            f.write(file_size[1].to_bytes(4, byteorder='big'))
            f.write(file_name.encode())
            f.write(file_size[0].to_bytes(8, byteorder='big'))
        
        #Write File Initialize
        f.write(headers.FILE_INDEX_START)
        f.write(headers.FILE_INDEX_START_PADDING)

        #write file data
        for file in index_data.keys():
            print("Writing file " + os.path.basename(file))
            with open(file, 'rb') as f2:
                f.write(f2.read())
        
        #Write File End
        f.write(headers.FILE_INDEX_END)
        f.write(headers.FILE_INDEX_END_PADDING)
        print("Done!")