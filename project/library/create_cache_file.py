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

#func to init file
def init_create_dump_folder(init_cat):
    src_dump_file = init_cat+'/dump.txt'
    f = open(src_dump_file, 'w', encoding='utf-8')
    print(init_cat)
    for (root, dirs, files) in os.walk(init_cat):
        for file in files:
            fullpath = os.path.join(root, file)
            fullpath = fullpath.replace('\\', '/')
            f.write(fullpath + ';' + check_sum(fullpath) + '\n')
          # tmp_file.append(fullpath + ';' + check_sum(fullpath))
    f.close()

def check_status(init_cat):
    src_dump_file = init_cat+'/dump.txt'
    file_tree_files=['']
    file_tree_src = ['']
    try:
        file_dump = open(src_dump_file, 'r', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не существует!')
    for file_line in file_dump:
        file_tree_files.append(file_line)
    print(init_cat)
    for (root, dirs, files) in os.walk(init_cat):
        for file in files:
            fullpath = os.path.join(root, file)
            fullpath = fullpath.replace('\\', '/')
            file_tree_src.append(fullpath)
    i=0
    file_tree_src.pop(0)
    print("Reading folder is done")
    print(len(file_tree_files))
    print('\n')
    print(len(file_tree_src))
    while i<len(file_tree_src):
        j = 0
        find_unidex_file = False
        while j<len(file_tree_files):
            file_orig = str(file_tree_files[j].split(';')[0])
            if str(file_tree_src[i])!=file_orig:
                find_unidex_file=True
            j += 1
        if find_unidex_file:
            print(file_tree_src[i]+'           '+file_orig+'\n')
        i+=1

    file_dump.close()
# init_cat='/Users/mcheryasov/code/private/code-python/'
init_cat='d:/tmp_book/'
#disable so it's init func
# init_create_dump_folder(init_cat)

check_status(init_cat)



#initialization variables
# init_cat='d:/data/Firefly/Фото/'


#compare one dir
# ext_file=['']
# tmp_file=['']
# itr=0
# tmp_file.pop(0)
#
# find_files=input("Input folders comma separated\n")
# find_files = find_files.replace('\\','/')
# init_cat=find_files.split(',')
#
# i=0
# while i< len(tmp_file):
#     file_orig=str(tmp_file[i].split(';')[1])
#     j = 0
#     while j < len(tmp_file):
#         file_comp = str(tmp_file[j].split(';')[1])
#         if i != j:
#             if str(file_comp) == str(file_orig):
#                 print('Found duplicate')
#                 print('File '+tmp_file[i].split(';')[0]+'  duplicate with  '+ tmp_file[j].split(';')[0]+'   '+tmp_file[i].split(';')[1] +'\n')
#         j += 1
#     i += 1
# # print("Job complete successfully")