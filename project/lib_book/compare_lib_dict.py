import os,hashlib

def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum

init_cat='d:/tmp_book/linux/'
# compare_cat='d:/Themes/Pictures/'
# init_cat='d:/data/Firefly/Фото/'
# init_cat='/home/knight/Network/'
contain=os.walk(init_cat)
# file_export = open('text_d.csv', 'w')
file_ar=[]
comp_file_ar=['']
dict_file={}
dict_all_files={}
for (root, dirs, files) in os.walk(init_cat):
    for file in files:
        fullpath = os.path.join(root,file)
        fullpath = fullpath.replace('\\','/')
        file_ar.append(fullpath)

# for item in file_ar:
#     print(item)
# print('\n\n\n\n\n\n')
i=0
while i<len(file_ar):
    print(file_ar[i])
    dict_file[0] = str(file_ar[i])
    dict_file[1] = str(os.path.getsize(file_ar[i]))
    dict_file[2] = str(check_sum(file_ar[i]))
    dict_all_files.update(ia='dict_file')
    i+=1
i=0
while i<len(dict_all_files):
    print(dict_all_files[i])
    i += 1
