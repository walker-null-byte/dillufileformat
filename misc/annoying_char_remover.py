def unicodetoascii(text):

    TEXT = (text.encode().
    		replace('\xe2\x80\x99'.encode(), "'".encode()).
            replace('\xc3\xa9'.encode(), 'e'.encode()).
            replace('\xe2\x80\x90'.encode(), '-'.encode()).
            replace('\xe2\x80\x91'.encode(), '-'.encode()).
            replace('\xe2\x80\x92'.encode(), '-'.encode()).
            replace('\xe2\x80\x93'.encode(), '-'.encode()).
            replace('\xe2\x80\x94'.encode(), '-'.encode()).
            replace('\xe2\x80\x94'.encode(), '-'.encode()).
            replace('\xe2\x80\x98'.encode(), "'".encode()).
            replace('\xe2\x80\x9b'.encode(), "'".encode()).
            replace('\xe2\x80\x9c'.encode(), '"'.encode()).
            replace('\xe2\x80\x9c'.encode(), '"'.encode()).
            replace('\xe2\x80\x9d'.encode(), '"'.encode()).
            replace('\xe2\x80\x9e'.encode(), '"'.encode()).
            replace('\xe2\x80\x9f'.encode(), '"'.encode()).
            replace('\xe2\x80\xa6'.encode(), '...'.encode()).
            replace('\xe2\x80\xb2'.encode(), "'".encode()).
            replace('\xe2\x80\xb3'.encode(), "'".encode()).
            replace('\xe2\x80\xb4'.encode(), "'".encode()).
            replace('\xe2\x80\xb5'.encode(), "'".encode()).
            replace('\xe2\x80\xb6'.encode(), "'".encode()).
            replace('\xe2\x80\xb7'.encode(), "'".encode()).
            replace('\xe2\x81\xba'.encode(), "+".encode()).
            replace('\xe2\x81\xbb'.encode(), "-".encode()).
            replace('\xe2\x81\xbc'.encode(), "=".encode()).
            replace('\xe2\x81\xbd'.encode(), "(".encode()).
            replace('\xe2\x81\xbe'.encode(), ")".encode())

                 )
    return TEXT.decode()

a = "BCSE205L – Module 2_Multiplication.pptx"

print(a.encode())
b=unicodetoascii(a)
print(b)
print(b.encode())