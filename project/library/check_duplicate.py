import os,hashlib

# Function get control sum
def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum

#initialization variables
# init_cat='d:/data/Firefly/Фото/'


#compare any dirs

#compare one dir
ext_file=['']
tmp_file=['']
itr=0
tmp_file.pop(0)

find_files=input("Input folders comma separated\n")
find_files = find_files.replace('\\','/')
init_cat=find_files.split(',')
# f = open('text.txt', 'w')
for item in init_cat:
    for (root, dirs, files) in os.walk(item):
        for file in files:
            fullpath = os.path.join(root,file)
            fullpath = fullpath.replace('\\','/')
            # f.write(fullpath+';'+check_sum(fullpath) + '\n')
            tmp_file.append(fullpath+';'+check_sum(fullpath))

i=0
# f.close()
while i< len(tmp_file):
    file_orig=str(tmp_file[i].split(';')[1])
    j = 0
    while j < len(tmp_file):
        file_comp = str(tmp_file[j].split(';')[1])
        if i != j:
            if str(file_comp) == str(file_orig):
                print('Found duplicate')
                print('File '+tmp_file[i].split(';')[0]+'  duplicate with  '+ tmp_file[j].split(';')[0]+'   '+tmp_file[i].split(';')[1] +'\n')
        j += 1
    i += 1
print("Job complete successfully")