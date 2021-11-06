import os,shutil

init_cat='d:/tmp_book/'
create_cat=init_cat+'Science/Mathematics/'

try:
    os.makedirs(create_cat)
except FileExistsError:
    print('Такой файл или каталог уже есть ' + create_cat)
except Exception:
    print('Это что ещё такое?')


tmp_file=['']
tmp_file.pop(0)
for (root, dirs, files) in os.walk(init_cat):
    for file in files:
        fullpath = os.path.join(root,file)
        fullpath = fullpath.replace('\\','/')
        tmp_file.append(fullpath)

for item in tmp_file:
    filename=str(os.path.split(item)[1]).lower()
    key="geom".lower()
    
    if str(key) in str(filename):
        dest=create_cat+str(os.path.split(item)[1]).lower()
        shutil.move(item,dest)
        print(dest)

