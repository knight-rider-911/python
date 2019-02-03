# import os
#
# def passage(file_name, folder):
#     for element in os.scandir(folder):
#         if element.is_file():
#             if element.name == file_name:
#                 yield folder
#         else:
#             yield from passage(file_name, element.path)
#
# print(*passage('md5.py', os.getcwd()))




# from os.path import join, getsize


# import os
# import fnmatch
# file_ext = '*.py'#расширение файлов для поиска
# path = '/home/knight/git/python/python/Douson/testing' #путь поиска вложенных файлов
# for dirs, files in os.walk(top=True):
#     for file_ext in files:
#         if fnmatch.fnmatch(name, file_ext):
#                 print ('name')



import os
for root, dirs, files in os.walk("/home/knight/git/python/python/Douson/testing", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   # print dir
   # for name in dirs:
   #    print(os.path.join(root, name))