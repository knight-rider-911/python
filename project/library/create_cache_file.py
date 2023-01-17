import os,hashlib, shutil


def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum



def init_tree(init_cat):
    file_tree_src_init = ['']
    print(init_cat)
    for (root, dirs, files) in os.walk(init_cat):
        for file in files:
            fullpath = os.path.join(root, file)
            fullpath = fullpath.replace('\\', '/')
            file_tree_src_init.append(fullpath)
    file_tree_src_init.pop(0)
    return file_tree_src_init


def init_create_dump_folder(init_cat):
    file_tree_src_init = init_tree(init_cat)
    src_dump_file = init_cat+'/dump.txt'

    f = open(src_dump_file, 'w', encoding='utf-8')
    print(init_cat+'\n')
    print(len(file_tree_src_init))
    i = 0
    while i<len(file_tree_src_init):
        f.write(file_tree_src_init[i] + ';' + check_sum(file_tree_src_init[i]) + '\n')
        if ((i/len(file_tree_src_init))*100) == 10:
            print("10%")
        elif ((i/len(file_tree_src_init))*100) == 20:
            print("20%")
        elif ((i/len(file_tree_src_init))*100) == 30:
            print("30%")
        elif ((i/len(file_tree_src_init))*100) == 40:
            print("40%")
        elif ((i/len(file_tree_src_init))*100) == 50:
            print("50%")
        elif ((i/len(file_tree_src_init))*100) == 60:
            print("60%")
        elif ((i/len(file_tree_src_init))*100) == 70:
            print("70%")
        elif ((i/len(file_tree_src_init))*100) == 80:
            print("80%")
        elif ((i/len(file_tree_src_init))*100) == 90:
            print("90%")
        elif ((i/len(file_tree_src_init))*100) == 100:
            print("100%")

        i += 1
    f.close()


def check_exist_file(init_cat):
    src_dump_file = init_cat + '/dump.txt'
    src_dump_new = init_cat + '/dumpnew.txt'
    src_dump_file_bckp = init_cat + '/dump.txt_bckp'
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
            file_tree_files.pop(i)
        i += 1
    file_dump.close()

    shutil.copy(src_dump_file, src_dump_file_bckp)
    print(len(file_tree_files))
    i = 0
    try:
        file_dump_fix = open(src_dump_file, 'w', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не существует!')
    while i<len(file_tree_files):
        file_dump_fix.write(file_tree_files[i])
        i += 1
    file_dump_fix.close()


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


def create_source_file_list(init_cat):
    file_tree_src_init = init_tree(init_cat)
    file_tree_src = ['']
    i = 0
    while i < len(file_tree_src_init):
        if ((i/len(file_tree_src_init))*100) == 10:
            print("10%")
        elif ((i/len(file_tree_src_init))*100) == 20:
            print("20%")
        elif ((i/len(file_tree_src_init))*100) == 30:
            print("30%")
        elif ((i/len(file_tree_src_init))*100) == 40:
            print("40%")
        elif ((i/len(file_tree_src_init))*100) == 50:
            print("50%")
        elif ((i/len(file_tree_src_init))*100) == 60:
            print("60%")
        elif ((i/len(file_tree_src_init))*100) == 70:
            print("70%")
        elif ((i/len(file_tree_src_init))*100) == 80:
            print("80%")
        elif ((i/len(file_tree_src_init))*100) == 90:
            print("90%")
        elif ((i/len(file_tree_src_init))*100) == 100:
            print("100%")
        file_tree_src.append(file_tree_src_init[i] + ';' + check_sum(file_tree_src_init[i]))
        i += 1
    file_tree_src.pop(0)
    return file_tree_src

def create_dump_file(init_cat):
    src_dump_file = init_cat + '/dump.txt'
    file_tree_files = ['']
    print(len(file_tree_files))
    try:
        file_dump = open(src_dump_file, 'r', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не существует!')
    for file_line in file_dump:
        file_tree_files.append(file_line)
    # file_tree_src = create_source_file_list(init_cat)
    file_tree_files.pop(0)
    i = 0
    src_dump_file = init_cat+'/dump.txt'
    f = open(src_dump_file, 'r', encoding='utf-8')
    output_duplicate_file = init_cat + '/out_duplicate.csv'
    file_duplicate = open(output_duplicate_file, 'w', encoding='utf-8')
    print(init_cat+'\n')
    print(len(file_tree_files))
    while i< len(file_tree_files):
        j = 0
        while j < len(file_tree_files):
            if (j != i) and (file_tree_files[i].split(';')[1] == file_tree_files[j].split(';')[1]):
                # print("Files is identic" + file_tree_files[i].split(';')[0] + file_tree_files[j].split(';')[0] )
                file_duplicate.write(str(file_tree_files[i].split(';')[0]) + ';' + str(file_tree_files[j].split(';')[0]) + '\n')
            # else:
            #     f.write(file_tree_src[i] + '\n')
            j += 1
        if ((i/len(file_tree_files))*100) == 10:
            print("10%")
        if ((i/len(file_tree_files))*100) == 20:
            print("20%")
        if ((i/len(file_tree_files))*100) == 30:
            print("30%")
        if ((i/len(file_tree_files))*100) == 40:
            print("40%")
        if ((i/len(file_tree_files))*100) == 50:
            print("50%")
        if ((i/len(file_tree_files))*100) == 60:
            print("60%")
        if ((i/len(file_tree_files))*100) == 70:
            print("70%")
        if ((i/len(file_tree_files))*100) == 80:
            print("80%")
        if ((i/len(file_tree_files))*100) == 90:
            print("90%")
        if ((i/len(file_tree_files))*100) == 100:
            print("100%")
        i += 1
    f.close()
    file_duplicate.close()




# init_cat='/Users/mcheryasov/code/private/code-python/'
init_cat='d:/tmp_book/'
#disable so it's init func
# init_create_dump_folder(init_cat)
# check_exist_file(init_cat)
# check_new_status(init_cat)

create_dump_file(init_cat)




print("Job complete successfully")