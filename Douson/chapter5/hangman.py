# Виселица
#
#Классическая игра "Виселица". Компьютер случайным образом выбирает слово.
#которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток. на экране появится фигурка повешенного.
# ~мпорт модуля
import random
# константы
HANGMAN = (
    """
        189
    """,
    """
        289
    """,
    """
        389
    """,
    """
        489
    """,
    """
        589
    """,
    """
        689
    """,
    """
        789
    """,
    """
        889
    """
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
# инициализация переменных
word = random.choice(WORDS) # слово для отгадывания
so_far = "-" * len(word) #по одному дефису на каждую букву. которую надо отгадать
wrong = 0 # количество ошибок. которые сделал игрок
used = [] # буквы. которые игрок уже предлагал
print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nBы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Bы уже предлагали букву", guess)
        guess = input("\n\nBвeдитe букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nДa! Буква", guess, "есть в слове!")
        # новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nK сожалению. буквы", guess, "нет в слове.")
        wrong += 1