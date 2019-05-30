import os

init_cat='d:/E-Book/E-book/Science'
contain=os.walk(init_cat)
# for item in os.walk(init_cat):
#     print(item)
# # print(contain[1])

# f = []
# for (dirpath, dirnames, filenames) in os.walk(init_cat):
#     f.extend(str(dirpath)+str(dirnames)+str(filenames))
#
# for item in f:
#     print(item)

# contain= os.listdir(init_cat)
# for i in contain:
#     print(i)
for (root, dirs, files) in os.walk(contain):
    print(files)
    # for dir in dirs:
    #     print(dir)

    # for _file in files:
    #     print(_file)