import os,hashlib



def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum



init_cat='d:/E-Book-new/E-book/DBMS, SQL/'
ext_file=['']
tmp_file=['']
itr=0
# init_cat='/home/knight/Network/'
contain=os.walk(init_cat)
for (root, dirs, files) in os.walk(init_cat):
    for file in files:
        fullpath = os.path.join(root,file)
        fullpath = fullpath.replace('\\','/')
        # print(fullpath)
        # print(file +'  ' + str(os.path.getsize(fullpath))+' checksum is'+check_sum(fullpath)+ '\n\n\n')
        tmp_file.append(os.path.splitext(fullpath)[1])


        # for item in ext_file:
        #     if str(os.path.splitext(fullpath)[1]) !=str(item):
        #         print('found ' + os.path.splitext(fullpath)[1]+' '+fullpath)
        #         ext_file.append(os.path.splitext(fullpath)[1])

for item in tmp_file:
    ext_file.append(tmp_file(item))
    print(len(ext_file))
    while itr <= len(ext_file):
        if str(item) != str(ext_file[itr]):
            ext_file.append(item)
        itr += 1


print('Файл'+file+'\n')


print('FOUND')
for newitem in ext_file:
    print(newitem)