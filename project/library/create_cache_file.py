import os,hashlib

# Function get control sum
import shutil


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

def check_exist_file(init_cat):
    src_dump_file = init_cat + '/dump.txt'
    file_tree_files = ['']
    try:
        file_dump = open(src_dump_file, 'r', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не существует!')
    for file_line in file_dump:
        file_tree_files.append(file_line)
    print(src_dump_file)
    file_tree_files.pop(0)
    i=0
    print(len(file_tree_files))
    while i<len(file_tree_files):
        if os.path.isfile(file_tree_files[i].split(';')[0])==False:
            print('File not exist'+file_tree_files[i].split(';')[0])
        i += 1


def check_new_status(init_cat):
    src_dump_file = init_cat+'/dump.txt'
    src_dump_file_bckp = init_cat+'/dump.txt_bck'
    file_tree_files=['']
    file_tree_src = ['']
    file_tree_files_pure = ['']
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
    file_tree_files.pop(0)
    print("Reading folder is done")
    #check remove or rename files

    i = 0
    print(len(file_tree_files))
    while i < len(file_tree_files):
        if os.path.isfile(file_tree_files[i].split(';')[0]) == False:
            print('File not exist: ' + file_tree_files[i].split(';')[0])
            file_tree_files.pop(i)
        i += 1
    print("End of check remove or rename files"+'\n')
    print(len(file_tree_files))

    print('Scan from file: '+str(len(file_tree_files))+'\n'+'Scan from folder: '+str(len(file_tree_src)))
    i = 0


    while i < len(file_tree_files):
        file_tree_files_pure.append(str(file_tree_files[i].split(';')[0]))
        i+=1
    file_tree_files_pure.pop(0)
    file_tree_src.sort()
    file_tree_files_pure.sort()
    print(len(file_tree_files_pure))
    print(len(file_tree_src))
    result = list(set(file_tree_src) - set(file_tree_files_pure))
    print(len(result))
    print(result)

    file_dump.close()
    shutil.copy(src_dump_file,src_dump_file_bckp)
    os.remove(src_dump_file_bckp)


# init_cat='/Users/mcheryasov/code/private/code-python/'
init_cat='d:/tmp_book/'
#disable so it's init func
#init_create_dump_folder(init_cat)
# check_exist_file(init_cat)
check_new_status(init_cat)




print("Job complete successfully")