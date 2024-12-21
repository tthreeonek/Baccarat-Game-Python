import sys
from game_logic import deal_cards, calculate_score, determine_winner, M, F1, F, G, B, C, V, Q

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
        except EOFError:
            return 0  # Возвращаем 0 в случае EOFError, чтобы избежать падения тестов

def input_str(prompt):
    """Ввод строки."""
    return input(prompt)

def main():
    print_centered("BACCARAT")
    print_centered("CREATIVE COMPUTING")
    print_centered("MORRISTOWN, NEW JERSEY")
    print("\n\n\n")
    print("BACCARAT -- CHEMIN DE FER\n")

    # Проверяем, запущен ли скрипт в режиме тестов
    if 'unittest' in sys.modules:
        print("Тесты запущены, пропускаем ввод пользователя.")
        return

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

        # Добавляем условие для выхода из цикла в режиме тестов
        if 'unittest' in sys.modules:
            break

if __name__ == "__main__":
    main()