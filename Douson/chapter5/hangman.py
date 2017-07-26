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
    89
    """
)#нарисовать висельника
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