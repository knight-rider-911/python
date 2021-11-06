import os,hashlib

def check_sum(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        str_check_sum=str(sha256_hash.hexdigest())
    return str_check_sum




init_cat='d:/data/telegeram/'
compare_cat='d:/Themes/Pictures/'
# init_cat='d:/data/Firefly/Фото/'
# init_cat='/home/knight/Network/'
contain=os.walk(init_cat)
# file_export = open('text_d.csv', 'w')
file_ar=[]
comp_file_ar=['']

for (root, dirs, files) in os.walk(init_cat):
    for file in files:
        fullpath = os.path.join(root,file)
        fullpath = fullpath.replace('\\','/')
        # print(fullpath)
        # print(file +'  ' + str(os.path.getsize(fullpath))+' checksum is'+check_sum(fullpath)+ '\n\n\n')
        file_ar.append(fullpath)
        # file_export.write(fullpath+';'\
        #                   + str(os.path.getsize(fullpath))+';'
        #                   + str(check_sum(fullpath))+';'+'\n'
        #                   )

# for (root, dirs, files) in os.walk(compare_cat):
#     for file in files:
#         fullpath = os.path.join(root,file)
#         fullpath = fullpath.replace('\\','/')
#         comp_file_ar.append(fullpath)
# i=0
# it=0
# while i < len(file_ar):
#     it = 0
#     while it<len(comp_file_ar):
#         if str(os.path.basename(file_ar[i]))==str(os.path.basename(comp_file_ar[it])):
#             print(str(file_ar[i])+'    '+str(comp_file_ar[it]))
#         it=it+1
#     # print(i)
#     i=i+1
# print(file_ar[3])
print("Check name\n\n\n")
# i=0
# while i < len(file_ar):
#     it=0
#     while it < len(file_ar):
#         if str(os.path.basename(file_ar[i]))==str(os.path.basename(file_ar[it])) and (i!=it):
#             print('Found for name '+ str(file_ar[i])+ '    and     '+str(file_ar[it])  +' checksum  '+ str(check_sum(file_ar[i])) )
#         it=it+1
#     i=i+1
#
# print("\n\n\nCheck size\n\n\n")
# i=0


# while i < len(file_ar):
#     it=0
#     while it < len(file_ar):
#         if str(os.path.getsize(file_ar[i]))==str(os.path.getsize(file_ar[it])) and (i!=it):
#             print('Found for name '+ str(file_ar[i])+ '    and     '+str(file_ar[it])  +' checksum  '+ str(check_sum(file_ar[i])) )
#         it=it+1
#     i=i+1
print('Cheksum check')
i=0
while i< len(file_ar):
    it=0
    while it < len(file_ar):
        if (str(check_sum(file_ar[i])) == str(check_sum(file_ar[it]))) and (i!=it):
            print('Found for name '+ str(file_ar[i])+ '    and     '+str(file_ar[it])  +' checksum  '+ str(check_sum(file_ar[i])) )
        print(it)
        it = it+1
    print('**************************************************************************************'+str(i))
    i=i+1
print('End file check')