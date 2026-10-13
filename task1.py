"""Программа подбирает правильную форму слова «гриб» по числу."""

mush = int(input("Введите количество грибов: "))

if mush < 0:
    print("Input error")
else:
    last_digit = mush % 10
    last_two = mush % 100
    word = "грибов"

    if 11 <= last_two <= 14:
        word = "грибов"
    elif last_digit == 1:
        word = "гриб"
    elif last_digit in (2, 3, 4):
        word = "гриба"
    else:
        word = "грибов"

    print(f"Мы собрали {mush} {word}")
