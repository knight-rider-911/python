# Крестики-нолики
# Компьютер играет в крестики-нолики против пользователя
# глобальные константы
X = "Х"
O = "O"
EMPTY = " "
ITE = "Ничья"
NUM_SQUARES = 9
def displау_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
    """
    Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех вреТвой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолиЧтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
доски - так. как показано ниже:
    0|1|2
    -----
    3|4|5
    -----
    6|7|8
    Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение. \n"""
    )
def ask_yes_no(question):
    """Задает вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ("у", "n"):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low. high):
        response = int(input(question))
    return response
def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
    if go_first =="у":
        print("\nHy что ж. даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nTвoя удаль тебя погубит. Буду начинать я.")
        computer = X
        human =O
    return computer, human