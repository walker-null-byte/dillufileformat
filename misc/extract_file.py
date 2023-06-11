from .list_files import list_files
from os import makedirs, chdir
from os.path import exists,dirname
def extract_file(filename, folder, data):
    print("Extracting file " + filename + " to " + folder + "...\n")
    
    #make new folder and extract there
    if not exists(folder):
        makedirs(folder)
        #change directory
        chdir(folder)
    else:
        print("Folder already exists. Do you want to overwrite? (y/n)")
        choice = input()
        if choice in 'Yy':
            chdir(folder)
        else:
            exit(0)
    
    f = open('../'+filename, 'rb')
    f.seek(data["offsets"][0])
    f.read(8)

    for file_name, file_size in list(data.items())[1:]:
        print("Extracting file " + file_name)
        file_data = f.read(file_size[0])
        makedirs(dirname(file_name), exist_ok=True)
        with open(file_name, 'wb') as f2:
            f2.write(file_data)
        