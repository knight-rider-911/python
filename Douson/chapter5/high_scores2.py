# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
    print(
    """
    Рекорды 2. О
    О - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    
    """

    )
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice =="0":
        print( "До свидания.")
    # вьвод таблицы рекордов
    elif choice == "1":
        print("Peкopды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score.name = entry
            print(name,"\t",score)
    # add а score
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Bnишитe его результат: "))
        entry = int(score.name)
        scores.append(entry )
        scores.sort(reverse=True)
        scores = scores[:5]  # в списке остается только 5 рекордов
    # непонятный пользовательский ввод
    else:
        print("Извините. в меню нет пункта",choice)
input("\n\nHaжмитe Enter. чтобы выйти.")