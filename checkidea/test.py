# const= list("432124050")
# print(const[0])
# new=()
# del const[0]
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# print(alphabet[2])
# const.reverse()
# new=const
# print(new)
# # for len(const)>0:
# #
# #     magicnumber = const [i]
# #     payload =
# # while len(payload)>0:


# alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# num = '432124050'

# def decode(s):
#     out=''
#     m = int(s[0])
#     s=s[:0:-1]
#     while len(s)>0:
#         ch_ = alphabet[int(s[:2] if len(s)>=2 else s[:1])-int(m)]
#         s=s[2:] if len(s)>=2 else s[1:]
#         out+=ch_
#     return out.capitalize()

# print(decode(num))

# from pathlib import Path
#
# home = str(Path.home())
# print(home)

# year = 1900
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print ('YES')
# else:
#     print ('NO')

