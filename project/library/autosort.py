import os,shutil

init_cat='d:/tmp_book/'
create_cat=init_cat+'Science/Mathematics/'
if os.path.exists(create_cat):
    if os.path.isfile(create_cat):
        print("It's file")
    if os.path.isdir(create_cat):
        print("It's directory")
else: 
    os.makedirs(create_cat)
    print("Directory was created")


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

