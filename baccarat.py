import random

# Глобальные переменные
M = [0] * 20  # Деньги игроков
F1 = [0] * 20  # Выбор игрока (банкир или игрок)
F = [0] * 20  # Ставки игроков
G = [""] * 20  # Имена игроков
B = [""] * 13  # Названия карт
V = [0] * 13  # Значения карт
A = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]  # Масти
Z = [[0 for _ in range(10)] for _ in range(9)]  # Таблица правил для банкира
W = [0] * 10  # Таблица правил для игрока
Q = [[0 for _ in range(13)] for _ in range(4)]  # Счетчик карт в колоде
C = [""] * 6  # Карты на столе

# Данные для карт
B = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

# Таблица правил для банкира
Z = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Таблица правил для игрока
W = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]


def print_centered(text, width=80):
    """Вывод текста по центру."""
    print(text.center(width))


def input_int(prompt):
    """Ввод целого числа с проверкой."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


def input_str(prompt):
    """Ввод строки."""
    return input(prompt)


def deal_cards():
    """Раздача карт."""
    global Q
    cards = []
    for _ in range(6):
        while True:
            suit = random.randint(0, 3)
            rank = random.randint(0, 12)
            if Q[suit][rank] < 32:
                Q[suit][rank] += 1
                cards.append((V[rank], f"{B[rank]} OF {A[suit]}"))
                break
    return cards


def calculate_score(hand):
    """Подсчет очков для руки."""
    total = sum(card[1] for card in hand)
    return total % 10


def determine_winner(player_score, banker_score):
    """Определение победителя."""
    if player_score > banker_score:
        return "PLAYER"
    elif banker_score > player_score:
        return "BANKER"
    else:
        return "TIE"


def main():
    print_centered("BACCARAT")
    print_centered("CREATIVE COMPUTING")
    print_centered("MORRISTOWN, NEW JERSEY")
    print("\n\n\n")
    print("BACCARAT -- CHEMIN DE FER\n")

    # Инструкции
    instructions = input("DO YOU NEED INSTRUCTIONS? (YES/NO): ").strip().upper()
    if instructions == "YES":
        print("    BACCARAT IS A VERY POPULAR GAME IN LAS")
        print("VEGAS.  THE PLAYER AND BANKER EACH RECEIVE")
        print("TWO CARDS FROM A 'SHOE' CONTAINING 8 DECKS")
        print("OF CARDS.   ALL CARD COMBINATIONS TOTALING")
        print("TEN ARE NOT COUNTED.  THE ONE THAT ENDS UP")
        print("CLOSER TO NINE WINS.  THE STAKES ARE HIGH,")
        print("ALL OF THE PLAYERS START WITH TEN THOUSAND")
        print("DOLLARS.  YOU CAN BET ON THE DEALER OR THE")
        print("PLAYER.   A THIRD CARD IS GIVEN ONLY UNDER")
        print("CERTAIN CONDITIONS, AS YOU WILL SEE.   LET")
        print("US BEGIN.      GOOD LUCK!\n")

    # Игроки
    P1 = input_int("HOW MANY PLAYERS? ")
    for J in range(P1):
        G[J] = input_str(f"WHAT IS THE NAME OF PLAYER {J + 1}? ")
        M[J] = 10000

    while True:
        # Раздача карт
        cards = deal_cards()
        for i in range(6):
            C[i] = cards[i][1]
            B[i] = cards[i][0]

        # Ставки
        for J in range(P1):
            if M[J] < 1:
                continue
            print(f"{G[J]} HAS ${M[J]}.   BET: ", end="")
            F[J] = input_int("")
            while F[J] > M[J] or F[J] < 1 or F[J] != int(F[J]):
                F[J] = input_int("INVALID BET. TRY AGAIN: ")
            print("(1) BANKER OR (2) PLAYER: ", end="")
            F1[J] = input_int("")
            while F1[J] not in [1, 2]:
                F1[J] = input_int("INVALID CHOICE. TRY AGAIN: ")

        # Подсчет очков
        T1 = B[1] + B[2]
        T2 = B[3] + B[4]
        if T1 >= 10:
            T1 -= 10
        if T2 >= 10:
            T2 -= 10

        print("\nBANKER\t\tPLAYER")
        print(f"{C[3]}\t\t{C[1]}")
        print(f"{C[4]}\t\t{C[2]}")
        print(f"PLAYERS TOTAL: {T1}")
        print(f"BANKERS TOTAL: {T2}\n")

        # Определение победителя
        if T2 > T1:
            winner = "BANKER"
        else:
            winner = "PLAYER"
        print(f"{winner} WINS!!\n")

        # Обновление денег игроков
        for J in range(P1):
            if M[J] <= 0:
                continue
            if F1[J] == (1 if winner == "BANKER" else 2):
                M[J] += F[J]
                print(f"{G[J]} WINS ${F[J]}, FOR A TOTAL OF ${M[J]}.")
            else:
                M[J] -= F[J]
                print(f"{G[J]} LOSES ${F[J]}, FOR A TOTAL OF ${M[J]}.")

        # Проверка на конец игры
        if all(m <= 0 for m in M[:P1]):
            print("THANK YOU FOR YOUR MONEY, AND THANK YOU FOR PLAYING.")
            break

        print("\n---------- NEW GAME ----------\n")


if __name__ == "__main__":
    main()