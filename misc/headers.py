versions = {
    "1.0.0"
}

FILE_HEADER_START = b"DILLU"
FILE_HEADER_PADDING = b"\x00\x00\x00"
FILE_HEADER_VERSION = b"1.0.0"
FILE_HEADER_VERSION_PADDING = b"\x00\x00\x00"

# Output File Info
# header_start(8) + header_verrsion(8) + file_size(8) + no_of_files(8)
# + file_index_start(8) + file_index_end(8)  
THIS_FILE_SIZE = 64


#Data Offset
OFFSET_START = 48
OFFSET_END = 0

#File Index
FILE_INDEX_START = b"FI"
FILE_INDEX_START_PADDING = b"\x00\x00\x00\x00\x00\x00"
FILE_INDEX_END = b"EI"
FILE_INDEX_END_PADDING = b"\x00\x00\x00\x00\x00\x00"

#File Index block size
FILE_INDEX_NAME_SIZE = b"\x00\x00\x00\xFF"
FILE_INDEX_SIZE_SIZE = b"\x00\x00\x00\x0F"

THIS_FILE_CHECKSUM = b"\x00\x00\x00\x00\x00\x00\x00\x00"