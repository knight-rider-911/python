import os,hashlib



def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum



# init_cat='d:/E-Book/E-book/Science'
init_cat='/home/knight/Network/'
contain=os.walk(init_cat)
file_export = open('text.csv', 'w')
for (root, dirs, files) in os.walk(init_cat):
    for file in files:
        fullpath = os.path.join(root,file)

        print(fullpath.replace('\\','/'))
        print(file +'  ' + str(os.path.getsize(fullpath))+' checksum is'+check_sum(fullpath)+ '\n\n\n')

        file_export.write(fullpath+';'\
                          + str(os.path.getsize(fullpath))+';'
                          + str(check_sum(fullpath))+';'+'\n'
                          )

file_export.close()