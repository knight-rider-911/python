#Арсенал героя 2.0
# Демонстрирует работу с кортежами
# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\n Итaк. в вашем арсенале: ")
for item in inventory:
    print(item)
input("\nHaжмитe Enter. чтобы продолжить.")
# найдем длину кортежа
print("Ceйчac в вашем распоряжении" , len(inventory), "предмета/-ов.")
input("\ nHaжмитe Enter. чтобы продолжить.")
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")
index = int(input("\nBвeдитe индекс одного из предметов арсенала: "))
print( "Под индексом", index, "в арсенале находится", inventory[index])
# отобразим срез
start = int(input("\nBвeдитe начальный индекс среза: "))
finish = int(input("Bвeдитe конечный индекс среза: "))
print("Cpeз inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\nHaжмитe Enter. чтобы продолжить.")